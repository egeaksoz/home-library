from typing import List
from fastapi import APIRouter, Depends
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from http import HTTPStatus

from app.database import get_session
from app.models import Library

library_router = APIRouter(prefix="/libraries", tags=["libraries"])

@library_router.get("/", response_model=List[Library])
async def read_libraries(session: AsyncSession = Depends(get_session)):
    """
    Get all libraries
    """
    libraries = await session.exec(select(Library))
    return libraries

@library_router.post("/", status_code=HTTPStatus.CREATED)
async def create_library(library: Library, session: AsyncSession = Depends(get_session)):
    """
    Create a new library
    """
    new_library = Library.model_validate(library)
    session.add(new_library)
    await session.commit()
    await session.refresh(new_library)
    return library
