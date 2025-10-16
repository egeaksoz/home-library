from fastapi import FastAPI

from app.database import create_db
from app.routes.library import library_router
from app.routes.book import book_router

app = FastAPI()
app.include_router(library_router)
app.include_router(book_router)
create_db()
