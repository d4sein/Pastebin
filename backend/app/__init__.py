from flask import Flask, Blueprint
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# Defines the WSGI application object
app = Flask(__name__)

# Configs
app.config.from_object('config')

# Defines the database object
db = SQLAlchemy(app)
# Defines the ODM object
ma = Marshmallow(app)

# Imports models from diffent blueprints
from app.paste.models import paste_models
from app.user.models import user_models
# Builds the database
db.create_all()

# Imports routes from different blueprints
from app.paste.controllers import paste_routes
from app.user.controllers import user_routes
