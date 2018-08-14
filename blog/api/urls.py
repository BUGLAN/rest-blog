from flask_restful import Api

from . import api_blueprint
from .views import (ArticleMethods, Articles, Categories, CategoryMethods,
                    Login, Manage, Page, TagMethods, UploadImage, megaArticle,
                    megaTags)

api = Api(api_blueprint)

api.add_resource(ArticleMethods, '/article')
api.add_resource(CategoryMethods, '/category')
api.add_resource(TagMethods, '/tag')
api.add_resource(Articles, '/articles')
api.add_resource(Categories, '/categories')
api.add_resource(Page, '/pages')
api.add_resource(Manage, '/manage')
api.add_resource(Login, '/login')
api.add_resource(megaTags, '/tags')
api.add_resource(megaArticle, '/mega_article')
api.add_resource(UploadImage, '/upload_image')
