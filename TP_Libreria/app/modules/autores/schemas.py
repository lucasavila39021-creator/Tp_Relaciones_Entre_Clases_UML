"""Schemas del módulo autores."""

from typing import Optional

from sqlmodel import SQLModel


class AutorBase(SQLModel):
    nombre: str
    apellido: str = ""


class AutorCreate(AutorBase):
    pass


class AutorRead(AutorBase):
    id: int


class AutorUpdate(SQLModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
