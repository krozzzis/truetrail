from fastapi import APIRouter, HTTPException, status
from datetime import datetime
from sqlalchemy.future import select
from typing import List

from models.activity import Activity, Action, Session
from models.schemas.activity import AddAction, AddSession

from db.database import SessionDep


router = APIRouter(prefix="/activities")


@router.get("/actions", response_model=List[Action])
async def get_actions(db: SessionDep):
    result = await db.execute(select(Action))
    sessions = result.scalars().all()
    return sessions


@router.get("/actions/{action_id}", response_model=Session)
async def get_action(action_id: int, db: SessionDep):
    action = await db.get(Action, action_id)

    if not action:
        raise HTTPException(status_code=404, detail="Action not found")

    return action


@router.post("/actions/", response_model=Action, status_code=status.HTTP_201_CREATED)
async def add_action(action: AddAction, db: SessionDep):
    new_action = Action(
        user_id=action.user_id,
        service_id=action.service_id,
        timestamp=session.start_time or datetime.now(),
        action_type=action.action_type,
    )

    db.add(new_action)
    await db.commit()

    return new_action


@router.get("/sessions", response_model=List[Session])
async def get_sessions(db: SessionDep):
    result = await db.execute(select(Session))
    sessions = result.scalars().all()
    return sessions


@router.get("/sessions/{session_id}", response_model=Session)
async def get_session(session_id: int, db: SessionDep):
    session = await db.get(Session, session_id)

    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    return session


@router.post("/sessions/", response_model=Session, status_code=status.HTTP_201_CREATED)
async def add_session(session: AddSession, db: SessionDep):
    new_session = Session(
        user_id=session.user_id,
        service_id=session.service_id,
        start_time=session.start_time or datetime.now(),
        end_time=session.end_time
    )

    db.add(new_session)
    await db.commit()

    return new_session
