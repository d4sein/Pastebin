from flask_restful import Resource

class Paste(Resource):
    def get(self):
        return {'hello': 'world'}
