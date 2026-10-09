"""Lógica de negocio del módulo clientes."""

from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.modules.clientes.models import Cliente
from app.modules.clientes.schemas import ClienteCreate, ClienteUpdate


async def list_clientes(session: AsyncSession) -> Sequence[Cliente]:
    result = await session.execute(select(Cliente))
    return result.scalars().all()


async def get_cliente(session: AsyncSession, cliente_id: int) -> Cliente | None:
    return await session.get(Cliente, cliente_id)


async def create_cliente(session: AsyncSession, data: ClienteCreate) -> Cliente:
    cliente = Cliente.model_validate(data)
    session.add(cliente)
    await session.commit()
    await session.refresh(cliente)
    return cliente


async def update_cliente(
    session: AsyncSession, cliente: Cliente, data: ClienteUpdate
) -> Cliente:
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(cliente, field, value)
    session.add(cliente)
    await session.commit()
    await session.refresh(cliente)
    return cliente


async def delete_cliente(session: AsyncSession, cliente: Cliente) -> None:
    await session.delete(cliente)
    await session.commit()
