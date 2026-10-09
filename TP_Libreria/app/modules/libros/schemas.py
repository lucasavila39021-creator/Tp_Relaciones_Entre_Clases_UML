"""Schemas del módulo libros."""

from typing import Optional

from sqlmodel import SQLModel


class LibroBase(SQLModel):
    titulo: str
    precio: float = 0.0
    stock: int = 0
    editorial_id: Optional[int] = None
    genero_id: Optional[int] = None
    autor_id: Optional[int] = None


class LibroCreate(LibroBase):
    pass


class LibroRead(LibroBase):
    id: int


class LibroUpdate(SQLModel):
    titulo: Optional[str] = None
    precio: Optional[float] = None
    stock: Optional[int] = None
    editorial_id: Optional[int] = None
    genero_id: Optional[int] = None
    autor_id: Optional[int] = None
