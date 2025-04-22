from sqlmodel import SQLModel, Field
from typing import Optional


class Service(SQLModel):
    id: int = Field(primary_key=True)
    name: Optional[str] = Field(default=None, index=True)
