from typing import Optional

from pydantic import BaseModel, UUID4


class UserCreate(BaseModel):
    name: str
    password: str
    role: str
    token: Optional[str] = None


class User(UserCreate):
    id: UUID4










class UserResponse(BaseModel):
    id: UUID4
    name: str
    role: str
    token: Optional[str]

    @classmethod
    def from_user(cls, user: User):
        return cls(
            id=user.id,
            name=user.name,
            role=user.role,
            token=user.token
        )


class UserLogin(BaseModel):
    name: str
    password: str
