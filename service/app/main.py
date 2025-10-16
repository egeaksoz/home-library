
from fastapi import FastAPI
from pydantic import BaseModel

from app.database import create_db
from app.routes.library import library_router

class Book(BaseModel):
    title: str
    author: str
    language: str
    genre: str
    cover: str
    read: bool
    description: str

app = FastAPI()
app.include_router(library_router)
create_db()

@app.get("/books/{book_name}")
def get_book(book_name: str):
    return {"message": f"Here is your book: {book_name}"}
    
@app.get("/books")
def get_books():
    return {"title": "My Name is Red", "author": "Orhan Pamuk", "language": "Turkish"}

@app.post("/books")
def add_book(book: Book):
    return book
