from sqlmodel import SQLModel
from datetime import datetime
from typing import Optional


class AddAction(SQLModel):
    user_id: int
    service_id: int
    timestamp: Optional[datetime]
    action_type: str


class AddSession(SQLModel):
    user_id: int
    service_id: int
    start_time: datetime
    end_time: Optional[datetime]
