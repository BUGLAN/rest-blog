from .views import ArticleMethods, CategoryMethods, TagMethods, Articles, Categories, Page, Mange
from flask_restful import Api
from . import api_blueprint

api = Api(api_blueprint)

api.add_resource(ArticleMethods, '/article')
api.add_resource(CategoryMethods, '/category')
api.add_resource(TagMethods, '/tag')
api.add_resource(Articles, '/articles')
api.add_resource(Categories, '/categories')
api.add_resource(Page, '/pages')
api.add_resource(Mange, '/mange')
