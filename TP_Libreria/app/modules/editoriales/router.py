"""Router del módulo editoriales."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.modules.editoriales.schemas import (
    EditorialCreate,
    EditorialRead,
    EditorialUpdate,
)
from app.modules.editoriales import service

router = APIRouter(prefix="/editoriales", tags=["editoriales"])


@router.get("", response_model=list[EditorialRead])
async def list_all(session: AsyncSession = Depends(get_session)):
    return await service.list_editoriales(session)


@router.get("/{editorial_id}", response_model=EditorialRead)
async def get_one(editorial_id: int, session: AsyncSession = Depends(get_session)):
    editorial = await service.get_editorial(session, editorial_id)
    if editorial is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return editorial


@router.post("", response_model=EditorialRead, status_code=status.HTTP_201_CREATED)
async def create(data: EditorialCreate, session: AsyncSession = Depends(get_session)):
    return await service.create_editorial(session, data)


@router.patch("/{editorial_id}", response_model=EditorialRead)
async def update(
    editorial_id: int,
    data: EditorialUpdate,
    session: AsyncSession = Depends(get_session),
):
    editorial = await service.get_editorial(session, editorial_id)
    if editorial is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return await service.update_editorial(session, editorial, data)


@router.delete("/{editorial_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(editorial_id: int, session: AsyncSession = Depends(get_session)):
    editorial = await service.get_editorial(session, editorial_id)
    if editorial is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    await service.delete_editorial(session, editorial)
