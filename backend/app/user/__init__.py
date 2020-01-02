from flask import Blueprint
from flask_restful import Api

user_bp = Blueprint('user_bp', __name__)
user_api = Api(user_bp)

from app.user import controllers, models, schemas
