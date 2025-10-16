from fastapi import APIRouter

from app.models import Book

book_router = APIRouter(prefix="/books", tags=["books"])

@book_router.get("/{book_name}")
def get_book(book_name: str):
    return {"message": f"Here is your book: {book_name}"}
        
@book_router.get("/")
def get_books():
    return {"title": "My Name is Red", "author": "Orhan Pamuk", "language": "Turkish"}

@book_router.post("/")
def add_book(book: Book):
    return book
