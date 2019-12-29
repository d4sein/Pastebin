from app import app
from app.paste import paste_bp, paste_api
from app.paste.controllers.paste_controller import Paste
from app.paste.controllers.edit_paste_controller import EditPaste


paste_api.add_resource(Paste, '/', endpoint='paste')
paste_api.add_resource(EditPaste, '/edit', endpoint='edit_paste')
app.register_blueprint(paste_bp)
