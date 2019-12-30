from app import app
from app.paste import paste_bp, paste_api

from app.paste.controllers.paste_controller import Paste


paste_api.add_resource(Paste, '/', endpoint='paste')
app.register_blueprint(paste_bp)
