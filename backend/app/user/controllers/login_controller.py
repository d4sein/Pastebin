from flask import request, session
from flask_restful import Resource
import marshmallow

from app import app, db
from app.user.models.user_model import User as UserDatabase, UserSchema


class Login(Resource):
    def get(self):
        return {}, 200

    def post(self):
        '''Stablishes a session for the user'''

        if 'username' in session:
            return {'log': 'Session has been already stablished'}, 202

        user_schema = UserSchema()

        try:
            user = user_schema.load(request.json)
        except marshmallow.exceptions.ValidationError as e:
            return {'error': e.args}, 400

        user_db = UserDatabase.query.filter_by(username=user.username).first()

        if user_db == None:
            return {'error': 'User not in database'}, 404

        if user.password != user_db.password:
            return {'error': 'Wrong password'}, 401

        user_session = {'username': user.username, 'password': user.password}
        session.update(user_session)

        return {'log': 'Session has been stablished'}, 200      

    def delete(self):
        '''Clears user session'''

        if 'username' in session:
            session.clear()
            return {'log': 'Session has been cleared'}, 200
        
        return {'log': 'Session has been already cleared'}, 202
