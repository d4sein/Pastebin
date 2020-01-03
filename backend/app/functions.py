from flask import request
import jwt

from app import app
from app.user.models.user_model import User as UserDatabase


def token_required(func):
    def wrapper(*args, **kwargs):
        token = request.headers['x-access-token'] if 'x-access-token' in request.headers else None
        
        if not token:
            return {'error': 'Token is missing'}, 401

        try:
            data = jwt.decode(token, app.secret_key)
            current_user = UserDatabase.query.filter_by(public_id=data['public_id']).first()
        except Exception as e:
            return {'error': f'Token is invalid {e}'}, 401

        return func(current_user, *args, **kwargs)

    return wrapper
