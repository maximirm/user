import hashlib
import secrets
from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repository.data_access import user_access
from app.repository.schemas import user_schema
from app.repository.schemas.user_schema import UserCreate, UserLogin, User, UserResponse


async def register_user(db: Session, user: UserCreate):
    user.password = __hash_password(user.password)
    await user_access.create_user(db, user)


async def authenticate_user(db: Session, login_data: UserLogin) -> User:
    user = await user_access.get_user_by_name(db, login_data.name)
    if user and __check_password(login_data.password, user.password):
        return user
    raise HTTPException(status_code=401, detail="Invalid credentials")


def generate_token() -> str:
    return secrets.token_urlsafe(32)


async def update_user_token(db: Session, user_id: str, token: str):
    await user_access.update_user_token(db, user_id, token)


async def get_user(db: Session, token: str) -> UserResponse:
    user = await user_access.get_user_by_token(db, token)
    if user:
        return UserResponse.from_user(user)
    raise HTTPException(
        status_code=404,
        detail=f"User with token {token} not found"
    )


async def get_all_users(db: Session) -> List[user_schema.UserResponse]:
    users = await user_access.get_all_users(db)
    if not users:
        raise HTTPException(
            status_code=404,
            detail="No users found",
        )
    return [user_schema.UserResponse.from_user(user) for user in users]


def __hash_password(password: str) -> str:
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def __check_password(plain_password: str, hashed_password: str) -> bool:
    return hashlib.sha256(plain_password.encode('utf-8')).hexdigest() == hashed_password
