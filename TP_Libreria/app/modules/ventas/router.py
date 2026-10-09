"""Router del módulo ventas."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.modules.ventas.schemas import VentaCreate, VentaRead, VentaUpdate
from app.modules.ventas import service

router = APIRouter(prefix="/ventas", tags=["ventas"])


@router.get("", response_model=list[VentaRead])
async def list_all(session: AsyncSession = Depends(get_session)):
    return await service.list_ventas(session)


@router.get("/{venta_id}", response_model=VentaRead)
async def get_one(venta_id: int, session: AsyncSession = Depends(get_session)):
    venta = await service.get_venta(session, venta_id)
    if venta is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return venta


@router.post("", response_model=VentaRead, status_code=status.HTTP_201_CREATED)
async def create(data: VentaCreate, session: AsyncSession = Depends(get_session)):
    return await service.create_venta(session, data)


@router.patch("/{venta_id}", response_model=VentaRead)
async def update(
    venta_id: int,
    data: VentaUpdate,
    session: AsyncSession = Depends(get_session),
):
    venta = await service.get_venta(session, venta_id)
    if venta is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return await service.update_venta(session, venta, data)


@router.delete("/{venta_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(venta_id: int, session: AsyncSession = Depends(get_session)):
    venta = await service.get_venta(session, venta_id)
    if venta is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    await service.delete_venta(session, venta)
