from fastapi import APIRouter, HTTPException, status
from sqlalchemy.future import select
from typing import List

from models.user import User
from models.schemas.user import CreateUser
from db.database import SessionDep


router = APIRouter()


@router.get("/users/", response_model=List[User])
async def get_users(db: SessionDep):
    result = await db.execute(select(User))
    users = result.scalars().all()
    return users


@router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int, db: SessionDep):
    user = await db.get(User, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@router.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: CreateUser, db: SessionDep):
    new_user = User(
        name=user.name,
    )

    db.add(new_user)
    await db.commit()

    return new_user
