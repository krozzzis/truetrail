from sqlmodel import SQLModel, Field
from typing import Optional


class Service(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: Optional[str] = Field(default=None, index=True)
