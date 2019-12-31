from flask import request, session
from flask_restful import Resource
import marshmallow

from app import app, db
from app.user.models.user_model import User as UserDatabase, UserSchema


class Register(Resource):
    def get(self):
        return {}, 200

    def post(self):
        '''Registers a new user'''

        if 'username' in session:
            return {'error': 'User already logged in'}, 409

        user_schema = UserSchema()

        try:
            user = user_schema.load(request.json)
        except marshmallow.exceptions.ValidationError as e:
            return {'error': e.args}, 400

        user_db = UserDatabase.query.filter_by(username=user.username).first()

        if user_db != None:
            return {'error': 'Username already in database'}, 409

        db.session.add(user)
        db.session.commit()

        user_session = {'username': user.username, 'password': user.password}
        session.update(user_session)

        return {'log': 'User has been registered'}, 201

    def delete(self):
        return {}, 202
