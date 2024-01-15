from typing import List

from fastapi import APIRouter, Depends, Header
from pydantic import UUID4
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from app.repository.config.database import get_db
from app.repository.schemas import user_schema
from app.services import user_service

router = APIRouter()


@router.post("/users/register")
async def register_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    await user_service.register_user(db, user)
    return JSONResponse(content="User created successfully", status_code=201)


@router.post("/users/login/")
async def login_user(login_data: user_schema.UserLogin, db: Session = Depends(get_db)):
    user = await user_service.authenticate_user(db, login_data)
    token = user_service.generate_token()
    await user_service.update_user_token(db, user.id, token)
    return JSONResponse(content={"token": token}, status_code=200)


@router.get("/users/", response_model=user_schema.UserResponse)
async def get_user(
        authorization: str = Header(..., description="Authorization token"),
        db: Session = Depends(get_db)
):
    token = authorization.split("Bearer ")[1]
    return await user_service.get_user(db, token)


@router.get("/users/all", response_model=List[user_schema.UserResponse])
async def get_all_users(db: Session = Depends(get_db)):
    return await user_service.get_all_users(db)


@router.delete("/users/{user_id}", response_model=str)
async def delete_user(user_id: UUID4, db: Session = Depends(get_db)):
    await user_service.delete_user(db, user_id)
    return JSONResponse(content=f"User with id {user_id} deleted successfully", status_code=200)

