import uuid

from sqlmodel.ext.asyncio.session import AsyncSession

from app.models import Book, Library

LIBRARY_1_UUID = uuid.uuid4()
LIBRARY_2_UUID = uuid.uuid4()
BOOK_1_UUID = uuid.uuid4()
BOOK_2_UUID = uuid.uuid4()
BOOK_3_UUID = uuid.uuid4()


class TestDatabase:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def populate_tables(self):
        library_1 = Library.model_validate(Library(id=LIBRARY_1_UUID, name="Library 1"))
        book_1 = Book.model_validate(
            Book(
                id=BOOK_1_UUID,
                title="Book 1",
                author="Author 1",
                library_id=LIBRARY_1_UUID,
            )
        )
        book_2 = Book.model_validate(
            Book(
                id=BOOK_2_UUID,
                title="Book 2",
                author="Author 2",
                library_id=LIBRARY_1_UUID,
            )
        )
        book_3 = Book.model_validate(
            Book(
                id=BOOK_3_UUID,
                title="Book 3",
                author="Author 3",
                library_id=LIBRARY_1_UUID,
            )
        )
        library_2 = Library.model_validate(Library(id=LIBRARY_2_UUID, name="Library 2"))
        self.session.add_all([library_1, library_2])
        await self.session.commit()
        self.session.add_all([book_1, book_2, book_3])
        await self.session.commit()
