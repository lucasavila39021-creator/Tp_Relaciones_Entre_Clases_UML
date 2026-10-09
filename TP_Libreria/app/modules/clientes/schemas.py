"""Schemas del módulo clientes."""

from typing import Optional

from sqlmodel import SQLModel


class ClienteBase(SQLModel):
    nombre: str
    email: str = ""


class ClienteCreate(ClienteBase):
    pass


class ClienteRead(ClienteBase):
    id: int


class ClienteUpdate(SQLModel):
    nombre: Optional[str] = None
    email: Optional[str] = None
