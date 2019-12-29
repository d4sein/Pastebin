from flask import Flask, Blueprint
from flask_cors import CORS
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Defines the WSGI application object
app = Flask(__name__)

# Configs
app.config.from_object('config')

# Enables CORS
CORS(app)
# Defines the database object
db = SQLAlchemy(app)
# Defines the ODM object
ma = Marshmallow(app)

# Imports blueprints
from app import paste
from app import user

# Builds the database
db.create_all()
