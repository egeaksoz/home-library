from typing import List
from fastapi import APIRouter, Depends
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

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

@library_router.post("/libraries")
def add_library(library: Library):
    return library
