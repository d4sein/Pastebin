from flask_restful import Resource

class DeletePaste(Resource):
    def get(self):
        return {'delete': 'paste'}
