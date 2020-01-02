from flask import request, session
from flask_restful import Resource
import marshmallow

from app import app, db

from app.user.models.user_model import User as UserDatabase
from app.user.schemas.user_schema import UserSchema


class User(Resource):
    def get(self):
        '''Returns a query for user(s)

        Parameters:
            id: str = `user id`
            username: str = `user name`
        '''

        args = request.args.to_dict()
        user_schema = UserSchema()

        # If length of args == 0 -> query for all users
        if len(args) == 0:
            users = UserDatabase.query.all()
            serialized_users = [user_schema.dump(user) for user in users]

            return {'users': serialized_users}, 200

        if len(args) == 1 and next(iter(args)) in ('id', 'username'):
            user = UserDatabase.query.filter_by(**args).first()
            serialized_user = user_schema.dump(user)

            if not len(serialized_user):
                return {'log': 'User not in database'}, 202

            return {'user': serialized_user}, 200

        return {'error': 'Wrong parameter'}, 400
