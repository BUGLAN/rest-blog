from .views import ArticleMethods
from flask_restful import Api
from . import api_blueprint


api = Api(api_blueprint)

api.add_resource(ArticleMethods, '/article')
