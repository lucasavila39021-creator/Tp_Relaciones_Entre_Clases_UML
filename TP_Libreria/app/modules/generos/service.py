"""Lógica de negocio del módulo generos."""

from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.modules.generos.models import Genero
from app.modules.generos.schemas import GeneroCreate, GeneroUpdate


async def list_generos(session: AsyncSession) -> Sequence[Genero]:
    result = await session.execute(select(Genero))
    return result.scalars().all()


async def get_genero(session: AsyncSession, genero_id: int) -> Genero | None:
    return await session.get(Genero, genero_id)


async def create_genero(session: AsyncSession, data: GeneroCreate) -> Genero:
    genero = Genero.model_validate(data)
    session.add(genero)
    await session.commit()
    await session.refresh(genero)
    return genero


async def update_genero(
    session: AsyncSession, genero: Genero, data: GeneroUpdate
) -> Genero:
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(genero, field, value)
    session.add(genero)
    await session.commit()
    await session.refresh(genero)
    return genero


async def delete_genero(session: AsyncSession, genero: Genero) -> None:
    await session.delete(genero)
    await session.commit()
