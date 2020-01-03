from flask import request, session
from flask_restful import Resource
import marshmallow

from app import app, db, functions

from app.user.models.user_model import User as UserDatabase
from app.user.schemas.user_schema import UserSchema


class User(Resource):
    @functions.token_required
    def get(current_user, self):
        '''
        Returns a query for user(s)

        Parameters:
            id: str = `User ID`
            username: str = `User name`
        '''

        if not current_user.admin:
            return {'error': 'Unauthorized user'}, 409

        args = request.args.to_dict()

        # If no args were passed -> query for all users
        if not args:
            users = UserDatabase.query.all()
            serialized_users = [UserSchema().dump(user) for user in users]

            return {'users': serialized_users}, 200

        # If length of args == 1, then there must be only one keyword in `args`
        # The keyword must be in set of possible keywords for query
        if len(args) == 1 and set(args).issubset({'id', 'username'}):
            user = UserDatabase.query.filter_by(**args).first()

            if not user:
                return {'log': 'User not in database'}, 202

            serialized_user = UserSchema().dump(user)
            return {'user': serialized_user}, 200

        return {'error': 'Wrong parameter'}, 400

    @functions.token_required
    def put(current_user, self):
        '''
        Updates `Admin` for user

        Parameters:
            username: str = `User name`
        '''

        if not current_user.admin:
            return {'error': 'Unauthorized user'}, 409

        args = request.args.to_dict()

        # If args is empty or keyword in args != `username`
        if not args or set(args) != set({'username'}):
            return {'error': 'Missing parameter `username`'}
    
        user = UserDatabase.query.filter_by(username=args['username']).first()
        user.admin = not user.admin
        db.session.commit()

        return {'log': f'`Admin` for {user.username} has been updated'}, 200

    @functions.token_required
    def delete(current_user, self):
        '''
        Deletes a user from database

        Parameters:
            username: str = `User name`
        '''

        if not current_user.admin:
            return {'error': 'Unauthorized user'}, 409

        args = request.args.to_dict()

        # If args is empty or keyword in args != `username`
        if not args or set(args) != set({'username'}):
            return {'error': 'Missing parameter `username`'}        

        user = UserDatabase.query.filter_by(username=args['username']).first()
        db.session.delete(user)
        db.session.commit()

        return {'log': 'User has been removed from database'}, 200
