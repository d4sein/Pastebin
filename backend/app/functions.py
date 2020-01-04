from flask import request
import jwt

from app import app
from app.user.models.user_model import User as UserDatabase


def token_required(func):
    def wrapper(*args, **kwargs):
        token = request.headers['x-access-token'] if 'x-access-token' in request.headers else None
        
        if not token:
            return {'error': 'Missing token'}, 401

        try:
            data = jwt.decode(token, app.secret_key)
        except Exception as e:
            return {'error': 'Invalid token'}, 401
        else:
            current_user = UserDatabase.query.filter_by(public_id=data['public_id']).first()

        return func(current_user, *args, **kwargs)

    return wrapper
