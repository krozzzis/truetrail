from sqlmodel import SQLModel
from typing import Optional


class CreateUser(SQLModel):
    name: Optional[str] = None
