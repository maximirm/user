from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.repository.models.user_model import User
from app.repository.schemas import user_schema


async def create_user(db: Session, user: user_schema.UserCreate):
    existing_user = db.execute(select(User).where(User.name == user.name))
    if existing_user.fetchone():
        raise HTTPException(
            status_code=400,
            detail="User with this name already exists",
        )

    db_user = User(**dict(user))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
