"""Lógica de negocio del módulo editoriales."""

from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.modules.editoriales.models import Editorial
from app.modules.editoriales.schemas import EditorialCreate, EditorialUpdate


async def list_editoriales(session: AsyncSession) -> Sequence[Editorial]:
    result = await session.execute(select(Editorial))
    return result.scalars().all()


async def get_editorial(session: AsyncSession, editorial_id: int) -> Editorial | None:
    return await session.get(Editorial, editorial_id)


async def create_editorial(
    session: AsyncSession, data: EditorialCreate
) -> Editorial:
    editorial = Editorial.model_validate(data)
    session.add(editorial)
    await session.commit()
    await session.refresh(editorial)
    return editorial


async def update_editorial(
    session: AsyncSession, editorial: Editorial, data: EditorialUpdate
) -> Editorial:
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(editorial, field, value)
    session.add(editorial)
    await session.commit()
    await session.refresh(editorial)
    return editorial


async def delete_editorial(session: AsyncSession, editorial: Editorial) -> None:
    await session.delete(editorial)
    await session.commit()
