from app import app
from app.user import user_bp, user_api

from app.user.controllers.user_controller import User
from app.user.controllers.session_controller import Session
from app.user.controllers.register_controller import Register


user_api.add_resource(User, '/user', endpoint='user')
user_api.add_resource(Session, '/session', endpoint='session')
user_api.add_resource(Register, '/register', endpoint='register')
app.register_blueprint(user_bp)
