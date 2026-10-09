"""Lógica de negocio del módulo autores."""

from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.modules.autores.models import Autor
from app.modules.autores.schemas import AutorCreate, AutorUpdate


async def list_autores(session: AsyncSession) -> Sequence[Autor]:
    result = await session.execute(select(Autor))
    return result.scalars().all()


async def get_autor(session: AsyncSession, autor_id: int) -> Autor | None:
    return await session.get(Autor, autor_id)


async def create_autor(session: AsyncSession, data: AutorCreate) -> Autor:
    autor = Autor.model_validate(data)
    session.add(autor)
    await session.commit()
    await session.refresh(autor)
    return autor


async def update_autor(
    session: AsyncSession, autor: Autor, data: AutorUpdate
) -> Autor:
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(autor, field, value)
    session.add(autor)
    await session.commit()
    await session.refresh(autor)
    return autor


async def delete_autor(session: AsyncSession, autor: Autor) -> None:
    await session.delete(autor)
    await session.commit()
