from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class Activity(SQLModel):
    user_id: int = Field(foreign_key="user.id")
    service_id: int = Field(foreign_key="service.id")


class Session(Activity, table=True):
    id: int = Field(primary_key=True)
    start_time: datetime
    end_time: Optional[datetime] = None


class Action(Activity, table=True):
    id: int = Field(primary_key=True)
    timestamp: datetime
    action_type: str
