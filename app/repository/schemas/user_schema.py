from typing import Optional

from pydantic import BaseModel, UUID4


class UserBase(BaseModel):
    name: str
    password: str
    role: int
    token: Optional[str] = None


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: UUID4

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    role: int
    token: Optional[str]


    class Config:
        orm_mode = True

    @classmethod
    def from_user(cls, user: User):
        return cls(role=user.role, token=user.token)


class UserLogin(BaseModel):
    name: str
    password: str

