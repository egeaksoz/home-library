from fastapi import APIRouter, Depends
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from http import HTTPStatus

from app.database import get_session
from app.models import Library

library_router = APIRouter(prefix="/libraries", tags=["libraries"])


@library_router.get("/", response_model=list[Library])
async def read_libraries(session: AsyncSession = Depends(get_session)) -> list[Library]:
    """
    Get all libraries
    """
    libraries = await session.exec(select(Library))
    return libraries


@library_router.get("/{library_id}", response_model=Library)
async def read_library(library_id: int, session: AsyncSession = Depends(get_session)):
    """
    Get library by ID
    """
    statement = select(Library).where(Library.id == library_id)
    library = await session.exec(statement)
    return library.first()


@library_router.post("/", status_code=HTTPStatus.CREATED)
async def create_library(
    library: Library, session: AsyncSession = Depends(get_session)
) -> Library:
    """
    Create a new library
    """
    new_library = Library.model_validate(library)
    session.add(new_library)
    await session.commit()
    await session.refresh(new_library)
    return library


@library_router.put("/{library_id}", status_code=HTTPStatus.OK)
async def update_library(
    library_id: int, library: Library, session: AsyncSession = Depends(get_session)
) -> Library:
    """
    Update an existing library
    """
    statement = select(Library).where(Library.id == library_id)
    results = await session.exec(statement)

    updated_library = results.one()
    updated_library.name = library.name
    await session.commit()
    await session.refresh(updated_library)

    return updated_library


@library_router.delete("/{library_id}", status_code=HTTPStatus.NO_CONTENT)
async def delete_library(
    library_id: int, session: AsyncSession = Depends(get_session)
) -> None:
    """
    Delete library by ID
    """
    statement = select(Library).where(Library.id == library_id)
    result = await session.exec(statement)
    library = result.first()
    await session.delete(library)
    await session.commit()
