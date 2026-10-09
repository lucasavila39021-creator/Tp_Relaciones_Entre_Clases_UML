"""Schemas del módulo editoriales."""

from typing import Optional

from sqlmodel import SQLModel


class EditorialBase(SQLModel):
    nombre: str


class EditorialCreate(EditorialBase):
    pass


class EditorialRead(EditorialBase):
    id: int


class EditorialUpdate(SQLModel):
    nombre: Optional[str] = None
