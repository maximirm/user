from app.repository.models.user_model import User as UserModel
from app.repository.schemas.user_schema import User as UserSchema


def convert_user_model_to_schema(model: UserModel) -> UserSchema:
    return UserSchema(
        id=str(model.id),
        name=model.name,
        password=model.password,
        role=model.role,
        token=model.token
    )
