from typing import List
from collections.abc import Sequence
from fastapi import APIRouter, Query
from sqlmodel import select

from app.database import SessionDep
from app.models import Library

library_router = APIRouter(prefix="/libraries", tags=["libraries"])

@library_router.get("/", response_model=List[Library])
def read_libraries(session: SessionDep, offset: int = 0, limit: int = Query(default=100, le=100)) -> Sequence[Library]:
    """
    Get all libraries
    """
    libraries = session.exec(select(Library).offset(offset).limit(limit)).all()
    return libraries

@library_router.post("/libraries")
def add_library(library: Library):
    return library
