from datetime import datetime, timedelta

from flask import request
from flask_restful import Resource
from werkzeug.security import generate_password_hash
import uuid
import sqlalchemy
import marshmallow
import jwt

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
                "password": `User password`,
                "password-confirm: `User password confirmation`
            }
        '''

        if request.authorization:
            return {'log': 'User already logged in'}, 409

        user_data = request.json

        if not set(user_data) == {'username', 'password', 'password-confirm'}:
            return {'error': f'Wrong parameters'}, 400
        
        # Verifies if password matches
        if user_data['password'] != user_data['password-confirm']:
            return {'error': 'Confirm password doesn\'t match password'}, 400
        
        # Generates public ID
        public_id = str(uuid.uuid4())
        user_data.update(public_id=public_id)
        # Generates hashed password
        hashed_password = generate_password_hash(user_data['password'], method='sha256')
        user_data.update(password=hashed_password)

        # Deletes password confirmation
        # It's not needed anymore
        del user_data['password-confirm']

        # Tries to validate user data
        try:
            user = UserSchema().load(user_data)
        except marshmallow.exceptions.ValidationError as e:
            return {'error': e.args}, 400

        db.session.add(user)
        # Tries to commit the user to the database
        # User `username` has a unique constraint
        try:
            db.session.commit()
        except sqlalchemy.exc.IntegrityError as e:
            return {'error': 'Username already in database'}, 409

        # Creates the auth token
        token = jwt.encode(
            {
                'public_id': user.public_id,
                'exp': datetime.utcnow() + timedelta(minutes=60)
            },
            app.secret_key
        )
        
        return {'token': token.decode('UTF-8')}, 201
