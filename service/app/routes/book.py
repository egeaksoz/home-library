import uuid
from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database import get_session
from app.models import Book

book_router = APIRouter(prefix="/libraries/{library_id}/books", tags=["books"])


@book_router.get("/", response_model=list[Book])
async def get_books(
    library_id: uuid.UUID, session: AsyncSession = Depends(get_session)
) -> list[Book]:
    """
    Get all books in a library.
    """

    statement = select(Book).where(Book.library_id == library_id)
    books = await session.exec(statement)
    return list(books)


@book_router.get("/{book_id}", response_model=Book)
async def get_book(
    book_id: uuid.UUID,
    library_id: uuid.UUID,
    session: AsyncSession = Depends(get_session),
) -> Book:
    """
    Get a book by its UUID.
    """
    statement = select(Book).where(Book.id == book_id and Book.library_id == library_id)
    book = await session.exec(statement)
    return book.one()


@book_router.post("/", status_code=HTTPStatus.CREATED)
async def add_book(
    book: Book, library_id: uuid.UUID, session: AsyncSession = Depends(get_session)
) -> Book:
    """
    Add a new book to a library.
    """
    book.library_id = library_id
    new_book = Book.model_validate(book)
    session.add(new_book)
    await session.commit()
    await session.refresh(new_book)
    return new_book


@book_router.put("/{book_id}", status_code=HTTPStatus.OK)
async def update_book(
    book_id: uuid.UUID,
    library_id: uuid.UUID,
    book: Book,
    session: AsyncSession = Depends(get_session),
) -> Book:
    """
    Update a book in a library.
    """
    statement = select(Book).where(Book.id == book_id and Book.library_id == library_id)
    book_to_update = await session.exec(statement)
    book_to_update = book_to_update.first()
    if book_to_update is None:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Book not found")
    for attr, value in book.model_dump().items():
        if value is not None:
            setattr(book_to_update, attr, value)
    await session.commit()
    await session.refresh(book_to_update)
    return book_to_update


@book_router.delete("/{book_id}", status_code=HTTPStatus.NO_CONTENT)
async def delete_book(
    book_id: uuid.UUID,
    library_id: uuid.UUID,
    session: AsyncSession = Depends(get_session),
) -> None:
    """
    Delete a book from a library.
    """
    statement = select(Book).where(Book.id == book_id and Book.library_id == library_id)
    book_to_delete = await session.exec(statement)
    book_to_delete = book_to_delete.first()
    if book_to_delete is None:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Book not found")
    await session.delete(book_to_delete)
    await session.commit()
