from datetime import datetime

from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=False, nullable=False)
    admin = db.Column(db.Boolean(), nullable=False, default=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    pastes = db.relationship('Paste', backref='user')
