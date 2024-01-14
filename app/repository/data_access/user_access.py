from sqlalchemy.orm import Session

from app.repository.models.user_model import User
from app.repository.schemas import user_schema


async def create_user(db: Session, user: user_schema.UserCreate):
    db_user = User(**dict(user))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
