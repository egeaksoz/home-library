import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database import get_session
from app.main import app

from .utils import TestDatabase

TEST_DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/test"


@pytest_asyncio.fixture(scope="function")
async def async_db_engine():
    async_engine = create_async_engine(TEST_DATABASE_URL, echo=False)

    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    yield async_engine
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)


@pytest_asyncio.fixture(scope="function")
async def async_db(async_db_engine):
    async_session = async_sessionmaker(
        expire_on_commit=False,
        autocommit=False,
        autoflush=False,
        bind=async_db_engine,
        class_=AsyncSession,
    )

    async with async_session() as session:
        await session.begin()

        yield session

        await session.rollback()


@pytest_asyncio.fixture(scope="function", autouse=True)
async def async_client(async_db) -> AsyncClient:
    db = TestDatabase(async_db)
    await db.populate_tables()

    def override_get_db():
        yield async_db

    app.dependency_overrides[get_session] = override_get_db
    return AsyncClient(
        transport=ASGITransport(app=app), base_url="http://localhost:8000"
    )
