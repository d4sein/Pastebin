from datetime import datetime

from app import db, ma
from app.paste.models.paste_model import Paste


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(30), unique=False, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    pastes = db.relationship('Paste', backref='user')


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
