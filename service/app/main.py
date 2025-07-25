from fastapi import FastAPI
from pydantic import BaseModel

class Book(BaseModel):
    title: str
    author: str
    language: str
    genre: str
    cover: str
    read: bool
    description: str

app = FastAPI()

@app.get("/books/{book_name}")
def get_book(book_name: str):
    return {"message": f"Here is your book: {book_name}"}
    
@app.get("/books")
def get_books():
    return {"title": "My Name is Red", "author": "Orhan Pamuk", "language": "Turkish"}

@app.post("/books")
def add_book(book: Book):
    return book
