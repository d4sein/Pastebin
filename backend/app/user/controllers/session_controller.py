from flask import request, session
from flask_restful import Resource
import marshmallow

from app import app, db

from app.user.models.user_model import User as UserDatabase
from app.user.schemas.user_schema import UserSchema


class Session(Resource):
    def post(self):
        '''
        Stablishes a session for user
        
        Body model:
            {
                "username": `the user name`,
                "password": `the user password`
            }
        '''

        # If session exists, then a user is already logged in
        if session:
            return {'log': 'Session has been already stablished'}, 202

        # Tries to validate user data
        try:
            user = UserSchema().load(request.json)
        except marshmallow.exceptions.ValidationError as e:
            return {'error': e.args}, 400

        # Verifies if user in database
        user_db = UserDatabase.query.filter_by(username=user.username).first()

        if not user_db:
            return {'error': 'User not in database'}, 404

        if user.password != user_db.password:
            return {'error': 'Wrong password'}, 401

        # Creates user session
        user_session = {'username': user.username, 'password': user.password}
        session.update(user_session)

        return {'log': 'Session has been stablished'}, 200

    def delete(self):
        '''Clears user session'''

        # If session, then user is logged in
        if session:
            # Clears the session
            session.clear()
            return {'log': 'Session has been cleared'}, 200
        
        return {'log': 'Session has been already cleared'}, 202
