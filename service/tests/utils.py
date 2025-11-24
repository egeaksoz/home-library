from sqlmodel.ext.asyncio.session import AsyncSession

from app.models import Book, Library


class TestDatabase:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def populate_tables(self):
        library_1 = Library.model_validate(Library(id=5, name="Library 1"))
        book_1 = Book.model_validate(
            Book(id=5, title="Book 1", author="Author 1", library_id=5)
        )
        book_2 = Book.model_validate(
            Book(id=6, title="Book 2", author="Author 2", library_id=5)
        )
        book_3 = Book.model_validate(
            Book(id=7, title="Book 3", author="Author 3", library_id=5)
        )
        library_2 = Library.model_validate(Library(id=6, name="Library 2"))
        self.session.add_all([library_1, library_2])
        await self.session.commit()
        self.session.add_all([book_1, book_2, book_3])
        await self.session.commit()
