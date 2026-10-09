"""Rutas HTTP del módulo editoriales: reciben, delegan y declaran la respuesta."""

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.modules.editoriales import service
from app.modules.editoriales.schemas import (
    EditorialCreate,
    EditorialRead,
    EditorialUpdate,
)

router = APIRouter(prefix="/editoriales", tags=["editoriales"])


@router.post("/", response_model=EditorialRead, status_code=status.HTTP_201_CREATED)
async def create(data: EditorialCreate, session: AsyncSession = Depends(get_session)):
    return await service.create_editorial(session, data)


@router.get("/", response_model=list[EditorialRead])
async def list_all(
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    session: AsyncSession = Depends(get_session),
):
    return await service.list_editoriales(session, limit, offset)


@router.get("/{editorial_id}", response_model=EditorialRead)
async def get_one(editorial_id: int, session: AsyncSession = Depends(get_session)):
    return await service.get_editorial(session, editorial_id)


@router.patch("/{editorial_id}", response_model=EditorialRead)
async def update(
    editorial_id: int,
    data: EditorialUpdate,
    session: AsyncSession = Depends(get_session),
):
    return await service.update_editorial(session, editorial_id, data)


@router.delete("/{editorial_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(editorial_id: int, session: AsyncSession = Depends(get_session)):
    await service.delete_editorial(session, editorial_id)