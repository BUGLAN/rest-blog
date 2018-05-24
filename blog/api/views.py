from extand import db
from blog.models import Article, Category, Tag, User
from flask_restful import Resource, marshal_with, fields, reqparse
from flask_sqlalchemy import sqlalchemy
from flask import current_app, jsonify
from blog.api.fields import article_category_fields, tags_fields, get_article_fields, get_category_fields, get_tag_fields, articles_fields, categories_fields
from blog.api.auth import auth
from sqlalchemy import and_


class ArticleMethods(Resource):
    def __init__(self):
        self.get_parser = reqparse.RequestParser()
        self.get_parser.add_argument(
            'slug',
            type=str,
            required=True,
            help='the argument cannot be blank')
        self.post_parser = reqparse.RequestParser()
        self.post_parser.add_argument(
            'slug',
            type=str,
            required=True,
            help='the argument cannot be blank')
        self.post_parser.add_argument(
            'title',
            type=str,
            required=True,
            help='the argument cannot be blank')
        self.post_parser.add_argument(
            'content',
            type=str,
            required=True,
            help='the argument cannot be blank')
        self.post_parser.add_argument(
            'category_id',
            type=int,
            required=True,
            help='the argument cannot be blank')
        self.post_parser.add_argument(
            'tag_ids',
            type=int,
            action='append',
            help='the argument cannot be blank')

        self.put_parser = reqparse.RequestParser()
        self.put_parser.add_argument(
            'id', type=int, required=True, help='the argument cannot be blank')

        self.put_parser.add_argument(
            'slug',
            type=str,
            required=True,
            help='the argument cannot be blank')
        self.put_parser.add_argument(
            'title',
            type=str,
            required=True,
            help='the argument cannot be blank')
        self.put_parser.add_argument(
            'content',
            type=str,
            required=True,
            help='the argument cannot be blank')
        self.put_parser.add_argument(
            'category_id',
            type=int,
            required=True,
            help='the argument cannot be blank')
        self.put_parser.add_argument(
            'tag_ids',
            type=int,
            action='append',
            help='the argument cannot be blank')

        self.delete_parser = reqparse.RequestParser()
        self.delete_parser.add_argument(
            'id', type=int, required=True, help='the argument cannot be blank')

    @marshal_with(get_article_fields)
    def get(self):
        args = self.get_parser.parse_args()
        article = Article.query.filter_by(slug=args['slug']).first_or_404()
        return article

    @auth.login_required
    def post(self):
        args = self.post_parser.parse_args()
        try:
            article = Article()
            article.title = args['title']
            article.slug = args['slug']
            article.content = args['content']
            article.category = Category.query.get(args['category_id'])
            article.tags = [
                Tag.query.get(id) for id in args['tag_ids']
                if Tag.query.get(id)
            ] if args['tag_ids'] else []
            # 相当于[None]如果Tag.query.get(id) 不存在的话
            db.session.add(article)
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            db.session.rollback()
            return {'status': 400, 'msg': '字段冲突'}, 400
        except sqlalchemy.exc.InvalidRequestError:
            db.session.rollback()
            return {'status': 400, 'msg': '字段冲突'}, 400
        return {'status': 200, 'msg': '新建文章成功'}

    @auth.login_required
    def put(self):
        args = self.put_parser.parse_args()
        article = Article.query.get_or_404(args['id'])
        try:
            article.title = args['title']
            article.slug = args['slug']
            article.content = args['content']
            article.category = Category.query.get(args['category_id'])
            article.tags = [
                Tag.query.get(id) for id in args['tag_ids']
                if Tag.query.get(id)
            ] if args['tag_ids'] else []
            # 相当于[None 如果Tag.query.get(id) 不存在的话]
            db.session.add(article)
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            return {'status': 400, 'msg': '字段冲突'}, 400
        except sqlalchemy.exc.InvalidRequestError:
            return {'status': 400, 'msg': '字段冲突'}, 400
        return {'status': 200, 'msg': '修改文章成功'}

    @auth.login_required
    def delete(self):
        args = self.delete_parser.parse_args()
        article = Article.query.get_or_404(args['id'])
        db.session.delete(article)
        db.session.commit()
        return {'status': 200, 'msg': '删除文章成功'}


class CategoryMethods(Resource):
    def __init__(self):
        self.get_parser = reqparse.RequestParser()
        self.get_parser.add_argument(
            'name',
            type=str,
            required=True,
            help='the argument cannot be blank')
        self.post_parser = reqparse.RequestParser()
        self.post_parser.add_argument(
            'name',
            type=str,
            required=True,
            help='the argument cannot be blank')
        self.post_parser.add_argument(
            'article_ids',
            type=int,
            action='append',
            help='the argument cannot be blank')

        self.put_parser = reqparse.RequestParser()
        self.put_parser.add_argument(
            'id', type=int, required=True, help='the argument cannot be blank')
        self.put_parser.add_argument(
            'name',
            type=str,
            required=True,
            help='the argument cannot be blank')
        self.put_parser.add_argument(
            'article_ids',
            type=int,
            action='append',
            help='the argument cannot be blank')

        self.delete_parser = reqparse.RequestParser()
        self.delete_parser.add_argument(
            'id', type=int, required=True, help='the argument cannot be blank')

    @marshal_with(get_category_fields)
    def get(self):
        args = self.get_parser.parse_args()
        category = Category.query.filter_by(name=args['name']).first_or_404()
        return category

    @auth.login_required
    def post(self):
        args = self.post_parser.parse_args()
        try:
            category = Category()
            category.name = args['name']
            category.articles = [
                Article.query.get(id) for id in args['article_ids']
                if Article.query.get(id)
            ] if args['article_ids'] else []
            db.session.add(category)
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            db.session.rollback()
            return {'status': 400, 'msg': '字段冲突'}, 400
        except sqlalchemy.exc.InvalidRequestError:
            db.session.rollback()
            return {'status': 400, 'msg': '字段冲突'}, 400
        return {'status': 200, 'msg': '新建分类成功'}

    @auth.login_required
    def put(self):
        args = self.put_parser.parse_args()
        category = Category.query.get_or_404(args['id'])
        try:
            category.name = args['name']
            category.articles = [
                Article.quert.get(id) for id in args['article_ids']
                if Article.query.get(id)
            ] if args['article_ids'] else []
            db.session.add(category)
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            return {'status': 400, 'msg': '字段冲突'}, 400
        except sqlalchemy.exc.InvalidRequestError:
            return {'status': 400, 'msg': '字段冲突'}, 400
        return {'status': 200, 'msg': '修该分类成功'}

    @auth.login_required
    def delete(self):
        args = self.delete_parser.parse_args()
        category = Category.query.get_or_404(args['id'])
        db.session.delete(category)
        db.session.commit()
        return {'status': 200, 'msg': '删除分类成功'}


class TagMethods(Resource):
    def __init__(self):
        self.get_parser = reqparse.RequestParser()
        self.get_parser.add_argument(
            'name',
            type=str,
            required=True,
            help='the argument cannot be blank')

        self.post_parser = reqparse.RequestParser()
        self.post_parser.add_argument(
            'name',
            type=str,
            required=True,
            help='the argument cannot be blank')
        self.post_parser.add_argument(
            'article_ids',
            type=int,
            action='append',
            help='the argument cannot be blank')

        self.put_parser = reqparse.RequestParser()
        self.put_parser.add_argument(
            'id', type=int, required=True, help='the argument cannot be blank')
        self.put_parser.add_argument(
            'name',
            type=str,
            required=True,
            help='the argument cannot be blank')
        self.put_parser.add_argument(
            'article_ids',
            type=int,
            action='append',
            help='the argument cannot be blank')

        self.delete_parser = reqparse.RequestParser()
        self.delete_parser.add_argument(
            'id', type=int, required=True, help='the argument cannot be blank')

    @marshal_with(get_tag_fields)
    def get(self):
        args = self.get_parser.parse_args()
        tag = Tag.query.filter_by(name=args['name']).first_or_404()
        return tag

    @auth.login_required
    def post(self):
        args = self.post_parser.parse_args()
        try:
            tag = Tag()
            tag.name = args['name']
            tag.articles = [
                Article.query.get(id) for id in args['article_ids']
                if Article.query.get(id)
            ] if args['article_ids'] else []
            db.session.add(tag)
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            db.session.rollback()
            return {'status': 400, 'msg': '字段冲突'}, 400
        except sqlalchemy.exc.InvalidRequestError:
            db.session.rollback()
            return {'status': 400, 'msg': '字段冲突'}, 400
        return {'status': 200, 'msg': '新建标签成功'}

    @auth.login_required
    def put(self):
        args = self.put_parser.parse_args()
        tag = Tag.query.get_or_404(args['id'])
        try:
            tag.name = args['name']
            tag.articles = [
                Article.query.get(id) for id in args['article_ids']
                if Article.query.get(id)
            ] if args['article_ids'] else []
            db.session.add(tag)
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            db.session.rollback()
            return {'status': 400, 'msg': '字段冲突'}, 400
        except sqlalchemy.exc.InvalidRequestError:
            db.session.rollback()
            return {'status': 400, 'msg': '字段冲突'}, 400
        return {'status': 200, 'msg': '新建标签成功'}

    @auth.login_required
    def delete(self):
        args = self.delete_parser.parse_args()
        tag = Tag.query.get_or_404(args['id'])
        db.session.delete(tag)
        db.session.commit()
        return {'status': 200, 'msg': '删除失败'}


class Articles(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument(
            'page',
            type=int,
        )

    @marshal_with(articles_fields)
    def get(self):
        args = self.parser.parse_args()
        page = args['page'] or 1
        items = current_app.config['PAGE_ITEMS']
        paginaton = Article.query.order_by(
            Article.create_time.desc()).paginate(page, items)
        return paginaton.items


class Categories(Resource):
    @marshal_with(categories_fields)
    def get(self):
        return Category.query.all()


class Page(Resource):
    def get(self):
        pages = Article.query.count()
        items = current_app.config['PAGE_ITEMS']
        page_num = pages // items
        if pages % items > 0:
            page_num += 1
        return {'pages': [page for page in range(1, page_num + 1)]}


class Mange(Resource):
    @auth.login_required
    def get(self):
        categories = [{
            'name': category.name,
            'id': category.id,
            'date': category.create_time.strftime('%Y-%m-%d')
        } for category in Category.query.all()]

        articles = [{
            'id':
            article.id,
            'title':
            article.title,
            'slug':
            article.slug,
            'category':
            article.category.name if article.category else '',
            'tags': [tag.name for tag in article.tags] if article.tags else [],
            'date':
            article.create_time.strftime('%Y-%m-%d')
        } for article in Article.query.all()]
        tags = [{
            'id': tag.id,
            'name': tag.name,
            'date': tag.create_time.strftime('%Y-%m-%d')
        } for tag in Tag.query.all()]
        return {
            'manage': {
                'categories': categories,
                'articles': articles,
                'tags': tags
            }
        }



class Login(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument(
                'username',
                type=str,
                required=True,
                help='this argument cannot be blank'
                )
        self.parser.add_argument(
                'password',
                type=str,
                required=True,
                help='this argument cannot be blank'
                )

    def post(self):
        args = self.parser.parse_args()
        user = User.query.filter(and_(User.name == args['username'], User.password==args['password'])).first_or_404()
        token = user.generate_auth_token().decode('ascii')
        return {'token': token}
