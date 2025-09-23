from typing import Annotated
from collections.abc import Sequence

from fastapi import Depends, FastAPI, Query
from pydantic import BaseModel
from sqlmodel import Session, select

from app.database import create_db, get_session
from app.models import Library

class Book(BaseModel):
    title: str
    author: str
    language: str
    genre: str
    cover: str
    read: bool
    description: str

app = FastAPI()
create_db()

SessionDep = Annotated[Session, Depends(get_session)]

@app.get("/v1/libraries")
def read_libraries(
    session: SessionDep,
    offset: int = 0,
    limit: int = Query(default=100, le=100)) -> Sequence[Library]:
    libraries = session.exec(select(Library).offset(offset).limit(limit)).all()
    return libraries

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
