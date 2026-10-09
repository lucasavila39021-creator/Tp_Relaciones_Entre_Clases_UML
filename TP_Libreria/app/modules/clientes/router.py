"""Router del módulo clientes."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.modules.clientes.schemas import ClienteCreate, ClienteRead, ClienteUpdate
from app.modules.clientes import service

router = APIRouter(prefix="/clientes", tags=["clientes"])


@router.get("", response_model=list[ClienteRead])
async def list_all(session: AsyncSession = Depends(get_session)):
    return await service.list_clientes(session)


@router.get("/{cliente_id}", response_model=ClienteRead)
async def get_one(cliente_id: int, session: AsyncSession = Depends(get_session)):
    cliente = await service.get_cliente(session, cliente_id)
    if cliente is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return cliente


@router.post("", response_model=ClienteRead, status_code=status.HTTP_201_CREATED)
async def create(data: ClienteCreate, session: AsyncSession = Depends(get_session)):
    return await service.create_cliente(session, data)


@router.patch("/{cliente_id}", response_model=ClienteRead)
async def update(
    cliente_id: int,
    data: ClienteUpdate,
    session: AsyncSession = Depends(get_session),
):
    cliente = await service.get_cliente(session, cliente_id)
    if cliente is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return await service.update_cliente(session, cliente, data)


@router.delete("/{cliente_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(cliente_id: int, session: AsyncSession = Depends(get_session)):
    cliente = await service.get_cliente(session, cliente_id)
    if cliente is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    await service.delete_cliente(session, cliente)
