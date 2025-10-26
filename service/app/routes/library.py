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

@library_router.put("/{library_id}", status_code=HTTPStatus.OK)
async def update_library(library_id: int, library: Library, session: AsyncSession = Depends(get_session)):
    """
    Update an existing library
    """
    statement = select(Library).where(Library.id == library_id)
    results = await session.exec(statement)
    
    updated_library = results.one()
    updated_library.name = library.name
    await session.commit()
    await session.refresh(updated_library)

    return updated_library
