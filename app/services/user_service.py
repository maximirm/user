from sqlalchemy.orm import Session

from app.repository.data_access import user_access
from app.repository.schemas.user_schema import UserCreate, UserResponse
from app.services.utils.converter import convert_user_model_to_schema


async def create_user(db: Session, user: UserCreate) -> UserResponse:
    user = await user_access.create_user(db, user)
    return UserResponse.from_user(convert_user_model_to_schema(user))
