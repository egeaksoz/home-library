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

class Library(BaseModel):
    name: str
    number_of_books: int

app = FastAPI()

@app.get("/v1/libraries")
def get_libraries():
    return {"libraries": "The Ezgi Library"}

@app.post("/v1/libraries")
def add_library(library: Library):
    return library

@app.get("/v1/books/{book_name}")
def get_book(book_name: str):
    return {"message": f"Here is your book: {book_name}"}
    
@app.get("/v1/books")
def get_books():
    return {"title": "My Name is Red", "author": "Orhan Pamuk", "language": "Turkish"}

@app.post("/v1/books")
def add_book(book: Book):
    return book
