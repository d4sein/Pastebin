from flask_restful import Resource

class EditPaste(Resource):
    def get(self):
        return {'edit': 'paste'}
