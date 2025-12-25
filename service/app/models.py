import uuid

from sqlmodel import Field, SQLModel


class Library(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str


class Book(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    library_id: uuid.UUID = Field(foreign_key="library.id")
    title: str
    author: str
    language: str | None = None
    genre: str | None = None
    cover: str | None = None
    read: bool | None = None
    description: str | None = None
