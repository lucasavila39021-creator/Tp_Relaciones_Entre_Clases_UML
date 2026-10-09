"""Router del módulo autores."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.modules.autores.schemas import AutorCreate, AutorRead, AutorUpdate
from app.modules.autores import service

router = APIRouter(prefix="/autores", tags=["autores"])


@router.get("", response_model=list[AutorRead])
async def list_all(session: AsyncSession = Depends(get_session)):
    return await service.list_autores(session)


@router.get("/{autor_id}", response_model=AutorRead)
async def get_one(autor_id: int, session: AsyncSession = Depends(get_session)):
    autor = await service.get_autor(session, autor_id)
    if autor is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return autor


@router.post("", response_model=AutorRead, status_code=status.HTTP_201_CREATED)
async def create(data: AutorCreate, session: AsyncSession = Depends(get_session)):
    return await service.create_autor(session, data)


@router.patch("/{autor_id}", response_model=AutorRead)
async def update(
    autor_id: int,
    data: AutorUpdate,
    session: AsyncSession = Depends(get_session),
):
    autor = await service.get_autor(session, autor_id)
    if autor is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return await service.update_autor(session, autor, data)


@router.delete("/{autor_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(autor_id: int, session: AsyncSession = Depends(get_session)):
    autor = await service.get_autor(session, autor_id)
    if autor is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    await service.delete_autor(session, autor)
