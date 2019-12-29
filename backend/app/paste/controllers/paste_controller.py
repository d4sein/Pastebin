from flask_restful import Resource
from flask import request

from app import app


class Paste(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        app.logger.info(request.data)
        return {'post': 'ok'}

    def put(self):
        app.logger.info(request.data)
        return {'put': 'ok'}

    def delete(self):
        return {'delete': 'ok'}
