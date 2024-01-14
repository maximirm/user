from fastapi import FastAPI

from app.api import user_controller
from app.repository.models import user_model
from app.repository.config.database import engine

user_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_controller.router, tags=["Users"])
