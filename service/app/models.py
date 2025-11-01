from sqlmodel import Field, SQLModel


class Library(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    number_of_books: int | None = None


class Book(SQLModel):
    title: str
    author: str
    language: str
    genre: str
    cover: str
    read: bool
    description: str
