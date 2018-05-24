from extand import db
from blog.models import Article, Category, Tag
from flask_restful import Resource, marshal_with, fields, reqparse
from flask_sqlalchemy import sqlalchemy

get_article_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'content': fields.String,
    'date': fields.DateTime
}


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
            required=True,
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
            required=True,
            help='the argument cannot be blank')

        self.delete_parser = reqparse.RequestParser()
        self.delete_parser.add_argument(
            'id', type=int, required=True, help='the argument cannot be blank')

    @marshal_with(get_article_fields)
    def get(self):
        args = self.get_parser.parse_args()
        article = Article.query.filter_by(slug=args['slug']).first()
        return article

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
            ]
            # 相当于[None 如果Tag.query.get(id) 不存在的话]
            db.session.add(article)
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            return {'status': 400, 'msg': '字段冲突'}, 400
        except sqlalchemy.exc.InvalidRequestError:
            return {'status': 400, 'msg': '字段冲突'}, 400
        return {'status': 200, 'msg': '新建文章成功'}

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
            ]
            # 相当于[None 如果Tag.query.get(id) 不存在的话]
            db.session.add(article)
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            return {'status': 400, 'msg': '字段冲突'}, 400
        except sqlalchemy.exc.InvalidRequestError:
            return {'status': 400, 'msg': '字段冲突'}, 400
        return {'status': 200, 'msg': '修改文章成功'}

    def delete(self):
        args = self.delete_parser.parse_args()
        article = Article.query.get_or_404(args['id'])
        db.session.delete(article)
        db.session.commit()
        return {'status': 200, 'msg': '删除文章成功'}
