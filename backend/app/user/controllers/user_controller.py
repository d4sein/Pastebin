from flask import request
from flask_restful import Resource

from app import app, db
from app.user.models.user_model import User as UserDatabase, UserSchema


class User(Resource):
    def get(self):
        user_schema = UserSchema()
        user_schema.dump()

    def post(self):
        return 200

    def put(self):
        app.logger.info(request.data)
        return 200
