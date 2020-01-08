from datetime import datetime
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

# Needs to come later because it makes use
# of PasteDatabase and PasteSchema
from app import functions


class Paste(Resource):
    @functions.token_required
    def get(current_user: UserDatabase, self):
        '''
        Returns a query for user paste(s)

        Parameters:
            username: str = `User name`,
            address: str = `Paste address`
        '''
        
        args = request.args.to_dict()

        if not args:
            return {'error': 'Parameter is empty'}, 400

        if set(args) == {'address'}:
            paste = PasteDatabase.query.filter_by(address=args['address']).first()
        
            if not paste:
                return {'error': 'Paste not in database'}, 400
            
            return {'title': paste.title, 'content': paste.content}, 200

        if set(args) == {'username'}:
            user = UserDatabase.query.filter_by(username=args['username']).first()

            if not user:
                return {'error': 'User not in database'}, 400

            if not user.id == current_user.id:
                if not current_user.admin:
                    return {'error': 'User cannot access pastes from other users'}, 403

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
        paste_data.update(address=address)

        # Verifies if user is logged in
        @functions.token_required
        def getUser(current_user: UserDatabase):
            return current_user

        user = getUser()
        if isinstance(user, UserDatabase):
            # Updates paste data with user ID
            paste_data.update(user_id=user.id)

        # Tries to validate paste data
        try:
            paste = PasteSchema().load(paste_data)
        except marshmallow.exceptions.ValidationError as e:
            return {'error': e.args}, 400

        # Adds paste to database
        db.session.add(paste)
        db.session.commit()

        return {'address': paste.address}, 201

    @functions.token_required
    def put(current_user: UserDatabase, self):
        '''
        Updates a paste from registered user

        Parameters:
            address: str = `Paste address`

        Body model:
            {
                "title": `Paste title`,
                "content": `Paste content`
            }
        '''

        args = request.args.to_dict()

        if not set(args) == {'address'}:
            return {'error': 'Missing parameter `address`'}, 400
        
        paste = PasteDatabase.query.filter_by(address=args['address']).first()

        if not paste:
            return {'error': 'Paste not in database'}, 404
        
        if not paste.user_id == current_user.id:
            if not current_user.admin:
                return {'error': 'User cannot update pastes from other users'}, 403

        paste_data = request.json
        paste_data.update(address=args['address'], last_edited=str(datetime.now()))

        if not paste_data['title'] or not paste_data['content']:
            return {'error': 'Inputs cannot be empty'}, 400

        # Tries to validate paste data
        try:
            valid_paste = PasteSchema().load(paste_data)
        except marshmallow.exceptions.ValidationError as e:
            return {'error': e.args}, 400

        paste.title = valid_paste.title
        paste.content = valid_paste.content
        paste.last_edited = valid_paste.last_edited

        db.session.commit()

        return {'log': 'Paste has been updated'}, 200

    @functions.token_required
    def delete(current_user: UserDatabase, self):
        '''
        Deletes a paste from database
        
        Parameters:
            address: str = `Paste address`
        '''

        args = request.args.to_dict()

        if not set(args) == {'address'}:
            return {'error': 'Missing parameter `address`'}, 400
        
        paste = PasteDatabase.query.filter_by(address=args['address']).first()

        if not paste:
            return {'error': 'Paste not in database'}, 404
        
        # If user is either Admin or owns the paste
        if current_user.admin or paste.user_id == current_user.id:
            db.session.delete(paste)
            db.session.commit()

            return {'log': 'Paste has been deleted'}, 200

        return {'error': 'User doesn\'t have permission to delete paste'}, 403
