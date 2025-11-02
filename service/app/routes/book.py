from fastapi import APIRouter, Depends
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from http import HTTPStatus

from app.database import get_session
from app.models import Book

book_router = APIRouter(prefix="/libraries/{library_id}/books", tags=["books"])


@book_router.get("/", response_model=list[Book])
async def get_books(library_id: int, session: AsyncSession = Depends(get_session)):
    """
    Get all books in a library.
    """
    statement = select(Book).where(Book.library_id == library_id)
    books = await session.exec(statement)
    return books


@book_router.get("/{book_id}", response_model=Book)
async def get_book(
    book_id: int, library_id: int, session: AsyncSession = Depends(get_session)
):
    """
    Get a book by its ID.
    """
    statement = select(Book).where(Book.id == book_id and Book.library_id == library_id)
    book = await session.exec(statement)
    return book.first()


@book_router.post("/", status_code=HTTPStatus.CREATED)
async def add_book(
    book: Book, library_id: int, session: AsyncSession = Depends(get_session)
):
    """
    Add a new book to a library.
    """
    book.library_id = library_id
    new_book = Book.model_validate(book)
    session.add(new_book)
    await session.commit()
    await session.refresh(new_book)
    return new_book
