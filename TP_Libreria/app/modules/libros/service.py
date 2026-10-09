"""Lógica de negocio del módulo libros."""

from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.modules.libros.models import Libro
from app.modules.libros.schemas import LibroCreate, LibroUpdate


async def list_libros(session: AsyncSession) -> Sequence[Libro]:
    result = await session.execute(select(Libro))
    return result.scalars().all()


async def get_libro(session: AsyncSession, libro_id: int) -> Libro | None:
    return await session.get(Libro, libro_id)


async def create_libro(session: AsyncSession, data: LibroCreate) -> Libro:
    libro = Libro.model_validate(data)
    session.add(libro)
    await session.commit()
    await session.refresh(libro)
    return libro


async def update_libro(
    session: AsyncSession, libro: Libro, data: LibroUpdate
) -> Libro:
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(libro, field, value)
    session.add(libro)
    await session.commit()
    await session.refresh(libro)
    return libro


async def delete_libro(session: AsyncSession, libro: Libro) -> None:
    await session.delete(libro)
    await session.commit()
