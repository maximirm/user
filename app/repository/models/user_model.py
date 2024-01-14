from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.repository.config.database import Base


class User(Base):
    __tablename__="users"
    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False, default=uuid.uuid4)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    role = Column(Integer, nullable=False)
    token = Column(String)
