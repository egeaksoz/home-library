from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.database import init_db
from app.routes.library import library_router
from app.routes.book import book_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(library_router)
app.include_router(book_router)
