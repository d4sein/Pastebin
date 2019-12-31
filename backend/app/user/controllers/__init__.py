from app import app
from app.user import user_bp, user_api

from app.user.controllers.login_controller import Login
from app.user.controllers.register_controller import Register


user_api.add_resource(Login, '/login', endpoint='login')
user_api.add_resource(Register, '/register', endpoint='register')
app.register_blueprint(user_bp)
