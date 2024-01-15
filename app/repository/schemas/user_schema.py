from typing import Optional

from pydantic import BaseModel, UUID4


class UserBase(BaseModel):
    name: str
    password: str
    role: str
    token: Optional[str] = None


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: UUID4

    class Config:
        from_attributes = True


class UserResponse(BaseModel):
    id: UUID4
    name: str
    role: str
    token: Optional[str]

    class Config:
        from_attributes = True

    @classmethod
    def from_user(cls, user: User):
        return cls(id=user.id, name=user.name, role=user.role, token=user.token)


class UserLogin(BaseModel):
    name: str
    password: str
