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

        # Parsing args
        args = request.args.to_dict()

        # If length of args == 0 -> query for all users
        if len(args) == 0:
            users = UserDatabase.query.all()
            serialized_users = [UserSchema().dump(user) for user in users]

            return {'users': serialized_users}, 200

        # If length of args == 1, then there must be only one keyword in `args`
        # `next(iter(args))` gets the first iterable in args
        # The keyword must be in tuple of possible keywords for query
        if len(args) == 1 and next(iter(args)) in ('id', 'username'):
            user = UserDatabase.query.filter_by(**args).first()

            if not user:
                return {'log': 'User not in database'}, 202

            serialized_user = UserSchema().dump(user)
            return {'user': serialized_user}, 200

        return {'error': 'Wrong parameter'}, 400
