from datetime import datetime

from app import db


class Paste(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(8), unique=True, nullable=False)
    title = db.Column(db.String(40), nullable=False)
    content = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    last_edited = db.Column(db.DateTime, nullable=True, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, default=0)
