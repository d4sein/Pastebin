from app import app
from app.user import user_bp, user_api
from app.user.controllers.user_controller import User


user_api.add_resource(User, '/', endpoint='user')
app.register_blueprint(user_bp)
