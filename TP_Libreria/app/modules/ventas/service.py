"""Lógica de negocio del módulo ventas."""

from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.modules.ventas.models import Venta
from app.modules.ventas.schemas import VentaCreate, VentaUpdate


async def list_ventas(session: AsyncSession) -> Sequence[Venta]:
    result = await session.execute(select(Venta))
    return result.scalars().all()


async def get_venta(session: AsyncSession, venta_id: int) -> Venta | None:
    return await session.get(Venta, venta_id)


async def create_venta(session: AsyncSession, data: VentaCreate) -> Venta:
    venta = Venta.model_validate(data)
    session.add(venta)
    await session.commit()
    await session.refresh(venta)
    return venta


async def update_venta(
    session: AsyncSession, venta: Venta, data: VentaUpdate
) -> Venta:
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(venta, field, value)
    session.add(venta)
    await session.commit()
    await session.refresh(venta)
    return venta


async def delete_venta(session: AsyncSession, venta: Venta) -> None:
    await session.delete(venta)
    await session.commit()
