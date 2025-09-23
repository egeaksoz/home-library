from sqlmodel import Field, SQLModel

class Library(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    number_of_books: int
