from fastapi import APIRouter, Depends
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.models import Book

book_router = APIRouter(prefix="/libraries/{library_id}/books", tags=["books"])


@book_router.get("/{book_name}")
def get_book(book_name: str):
    return {"message": f"Here is your book: {book_name}"}


@book_router.get("/", response_model=list[Book])
async def get_books(library_id: int, session: AsyncSession = Depends(get_session)):
    """
    Get all books in a library.
    """
    statement = select(Book).where(Book.library_id == library_id)
    books = await session.exec(statement)
    return books


@book_router.post("/")
def add_book(book: Book):
    return book
