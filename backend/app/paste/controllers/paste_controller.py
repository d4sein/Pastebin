import random
from string import ascii_letters

from flask import request, session
from flask_restful import Resource
import marshmallow

from app import app, db

from app.paste.models.paste_model import Paste as PasteDatabase
from app.paste.schemas.paste_schema import PasteSchema

from app.user.models.user_model import User as UserDatabase
from app.user.schemas.user_schema import UserSchema


class Paste(Resource):
    def get(self):
        '''
        Returns a query for user pastes

        Parameters:
            username: str = `User name`
        '''
        
        args = request.args.to_dict()

        if not args:
            return {'error': 'Parameter is empty'}, 400
        
        if next(iter(args)) == 'username':
            user = UserDatabase.query.filter_by(username=args['username']).first()

            if not user:
                return {'error': 'User not in database'}, 400

            pastes = PasteDatabase.query.filter_by(user_id=user.id).all()
            pastes_data = list()

            for paste in pastes:
                temp_data = {
                    'address': paste.address,
                    'title': paste.title,
                    'created': paste.created.strftime('%m/%d/%Y-%H:%M:%S'),
                    'last_edited': paste.last_edited.strftime('%m/%d/%Y-%H:%M:%S')
                }

                pastes_data.append(temp_data)
            
            return {'pastes': pastes_data}, 200
        
        return {'error': 'Wrong parameters'}, 400

    def post(self):
        '''
        Creates a new paste

        Body model:
            {
                "title": `Paste title`,
                "content": `Paste content`
            }
        '''
        while True:
            # Generates a random address
            address = ''.join(random.choice(ascii_letters) for i in range(8))
            db_address = PasteDatabase.query.filter_by(address=address).first()

            # If paste address is unique
            if address != db_address:
                break

        paste_data = request.json
        # Updates paste data with unique address
        paste_data.update({'address': address})

        # If session exists, get user
        if session:
            user = UserDatabase.query.filter_by(username=session['username']).first()
            # Updates paste data with user ID
            paste_data.update({'user_id': user.id})

        # Tries to validate paste data
        try:
            paste = PasteSchema().load(paste_data)
        except marshmallow.exceptions.ValidationError as e:
            return {'error': e.args}, 400

        # Adds paste to database
        db.session.add(paste)
        db.session.commit()

        return {'log': 'Paste has been created'}, 201
