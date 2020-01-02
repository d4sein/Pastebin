import random
from string import ascii_letters

from flask import request, session
from flask_restful import Resource

from app import app, db

from app.paste.models.paste_model import Paste as PasteDatabase
from app.paste.schemas.paste_schema import PasteSchema

from app.user.models.user_model import User as UserDatabase
from app.user.schemas.user_schema import UserSchema


class Paste(Resource):
    def get(self):
        return {'paste': 'foi'}, 200

    def post(self):
        while True:
            address = ''.join(random.choice(ascii_letters) for i in range(8))
            db_address = PasteDatabase.query.filter_by(address=address).first()

            # If paste address is unique
            if address != db_address:
                break

        paste_data = request.json
        # Updates paste with unique address
        paste_data.update({'address': address})

        if session:
            user = UserDatabase.query.filter_by(username=session['username']).first()
            paste_data.update({'user_id': user.id})

        try:
            paste = PasteSchema().load(paste_data)
        except ma.exceptions.ValidationError as e:
            return {'error': e.args}, 400

        db.session.add(paste)
        db.session.commit()

        return {'log': 'Paste has been created'}, 201
