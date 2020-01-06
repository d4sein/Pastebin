from datetime import datetime, timedelta

from flask import request, session
from flask_restful import Resource
from werkzeug.security import check_password_hash
import marshmallow
import jwt

from app import app, db, functions
from app.user.models.user_model import User as UserDatabase
from app.user.schemas.user_schema import UserSchema


class Session(Resource):
    @functions.token_required
    def get(current_user: UserDatabase, self):
        '''Gets current user'''

        return {'username': current_user.username}, 200

    def post(self):
        '''
        Creates an auth token for user
        
        Body model:
            {
                "username": `User name`,
                "password": `User password`
            }
        '''

        auth = request.authorization

        if not auth or not auth.username or not auth.password:
            return {'error': 'Failed to verify authentication'}, 401

        user = UserDatabase.query.filter_by(username=auth.username).first()

        if not user:
            return {'error': 'User not in database'}, 404

        if not check_password_hash(user.password, auth.password):
            return {'error': 'Failed to authenticate user'}, 401

        # Creates the auth token
        token = jwt.encode(
            {
                'public_id': user.public_id,
                'exp': datetime.utcnow() + timedelta(minutes=60)
            },
            app.secret_key
        )
        
        return {'token': token.decode('UTF-8')}, 200
