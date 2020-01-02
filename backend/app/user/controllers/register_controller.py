from flask import request, session
from flask_restful import Resource
import sqlalchemy
import marshmallow

from app import app, db

from app.user.models.user_model import User as UserDatabase
from app.user.schemas.user_schema import UserSchema


class Register(Resource):
    def post(self):
        '''
        Registers a new user
        
        Body model:
            {
                "username": `User name`,
                "password": `User password`
            }
        '''

        # If session exists, then there is a user logged in
        if session:
            return {'error': 'User already logged in'}, 409

        # Tries to validate user data
        try:
            user = UserSchema().load(request.json)
        except marshmallow.exceptions.ValidationError as e:
            return {'error': e.args}, 400

        db.session.add(user)
        # Tries to commit the user to the database
        # User `username` has a unique constraint
        try:
            db.session.commit()
        except sqlalchemy.exc.IntegrityError as e:
            return {'error': 'Username already in database'}, 409

        # Creates a session for the newly registered user
        user_session = {'username': user.username, 'password': user.password}
        session.update(user_session)

        return {'log': 'User has been registered'}, 201
