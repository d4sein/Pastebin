import random
from string import ascii_letters

from flask import request
from flask_restful import Resource

from app import app, db
from app.paste.models.paste_model import Paste as PasteDatabase
from app.user.models.user_model import User as UserDatabase, UserSchema


class Paste(Resource):
    def get(self):
        return 200

    def post(self):
        # user_schema = UserSchema()
        # result = user_schema.load(request.data)
        # app.logger.info(result)

        return 200

    def put(self):
        while True:
            address = ''.join(random.choice(ascii_letters) for i in range(8))
            db_address = PasteDatabase.query.filter_by(address=address).first()

            if address != db_address:
                break

        user = UserDatabase.query.filter_by(username='d4sein').first()
        paste = PasteDatabase(address=address, user_id=user.id)

        db.session.add(paste)
        db.session.commit()

        return 200
