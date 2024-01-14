from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.repository.config.database import get_db
from app.repository.schemas import user_schema
from app.services import user_service

router = APIRouter()


@router.post("/users/", response_model=user_schema.UserResponse)
async def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    return await user_service.create_user(db, user)
