from fastapi import HTTPException
from sqlalchemy import select, update
from sqlalchemy.orm import Session

from app.repository.models.user_model import User
from app.repository.schemas import user_schema


async def create_user(db: Session, user: user_schema.UserCreate):
    existing_user = await get_user_by_name(db, user.name)
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="User with this name already exists",
        )
    db_user = User(**dict(user))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)


async def get_user_by_name(db: Session, name: str):
    return db.execute(select(User).where(User.name == name)).scalar_one_or_none()


async def update_user_token(db: Session, user_id: str, token: str):
    db.execute(update(User).where(User.id == user_id).values(token=token))
    db.commit()


async def get_user_by_token(db: Session, token: str) -> User:
    return db.execute(select(User).where(User.token == token)).scalar_one_or_none()



