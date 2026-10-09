"""Schemas del módulo generos."""

from typing import Optional

from sqlmodel import SQLModel


class GeneroBase(SQLModel):
    nombre: str


class GeneroCreate(GeneroBase):
    pass


class GeneroRead(GeneroBase):
    id: int


class GeneroUpdate(SQLModel):
    nombre: Optional[str] = None
