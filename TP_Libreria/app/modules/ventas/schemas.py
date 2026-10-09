"""Schemas del módulo ventas."""

from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel


class VentaBase(SQLModel):
    cliente_id: Optional[int] = None
    libro_id: Optional[int] = None
    cantidad: int = 1


class VentaCreate(VentaBase):
    pass


class VentaRead(VentaBase):
    id: int
    fecha: datetime


class VentaUpdate(SQLModel):
    cliente_id: Optional[int] = None
    libro_id: Optional[int] = None
    cantidad: Optional[int] = None
