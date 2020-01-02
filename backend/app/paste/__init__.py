from flask import Blueprint
from flask_restful import Api

paste_bp = Blueprint('paste_bp', __name__, url_prefix='/paste')
paste_api = Api(paste_bp)

from app.paste import controllers, models, schemas
