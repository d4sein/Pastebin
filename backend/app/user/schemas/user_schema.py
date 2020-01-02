from app import ma

from app.user.models.user_model import User


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
