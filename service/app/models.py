from sqlmodel import Field, SQLModel


class Library(SQLModel, table=True):
    id: int | None = Field(primary_key=True)
    name: str


class Book(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    library_id: int | None = Field(default=None, foreign_key="library.id")
    title: str
    author: str
    language: str | None = None
    genre: str | None = None
    cover: str | None = None
    read: bool | None = None
    description: str | None = None
