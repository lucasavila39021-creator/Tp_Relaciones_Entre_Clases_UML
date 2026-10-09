"""Router del módulo generos."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.modules.generos.schemas import GeneroCreate, GeneroRead, GeneroUpdate
from app.modules.generos import service

router = APIRouter(prefix="/generos", tags=["generos"])


@router.get("", response_model=list[GeneroRead])
async def list_all(session: AsyncSession = Depends(get_session)):
    return await service.list_generos(session)


@router.get("/{genero_id}", response_model=GeneroRead)
async def get_one(genero_id: int, session: AsyncSession = Depends(get_session)):
    genero = await service.get_genero(session, genero_id)
    if genero is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return genero


@router.post("", response_model=GeneroRead, status_code=status.HTTP_201_CREATED)
async def create(data: GeneroCreate, session: AsyncSession = Depends(get_session)):
    return await service.create_genero(session, data)


@router.patch("/{genero_id}", response_model=GeneroRead)
async def update(
    genero_id: int,
    data: GeneroUpdate,
    session: AsyncSession = Depends(get_session),
):
    genero = await service.get_genero(session, genero_id)
    if genero is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return await service.update_genero(session, genero, data)


@router.delete("/{genero_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(genero_id: int, session: AsyncSession = Depends(get_session)):
    genero = await service.get_genero(session, genero_id)
    if genero is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    await service.delete_genero(session, genero)
