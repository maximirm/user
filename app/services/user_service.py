import hashlib
import secrets

from sqlalchemy.orm import Session

from app.repository.data_access import user_access
from app.repository.schemas.user_schema import UserCreate, UserLogin, User


async def register_user(db: Session, user: UserCreate):
    user.password = __hash_password(user.password)
    await user_access.create_user(db, user)


async def authenticate_user(db: Session, login_data: UserLogin) -> User:
    user = await user_access.get_user_by_name(db, login_data.name)
    if user and __check_password(login_data.password, user.password):
        return user
    return None


def generate_token() -> str:
    return secrets.token_urlsafe(32)


async def update_user_token(db: Session, user_id: str, token: str):
    await user_access.update_user_token(db, user_id, token)


def __hash_password(password: str) -> str:
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def __check_password(plain_password: str, hashed_password: str) -> bool:
    return hashlib.sha256(plain_password.encode('utf-8')).hexdigest() == hashed_password
