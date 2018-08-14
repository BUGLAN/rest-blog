from flask_restful import fields

article_category_fields = {'id': fields.Integer, 'name': fields.String}

tags_fields = {'id': fields.Integer, 'name': fields.String}

get_article_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'content': fields.String,
    'raw_content': fields.String,
    'slug': fields.String,
    'date':
    fields.String(attribute=lambda x: x.create_time.strftime('%Y-%m-%d')),
    'category': fields.Nested(article_category_fields),
    'tags': fields.List(fields.Nested(tags_fields))
}

get_category_fields = {'id': fields.Integer, 'name': fields.String}

get_tag_fields = {'id': fields.Integer, 'name': fields.String}

articles_fields = {
    'id':
    fields.Integer,
    'title':
    fields.String,
    'content':
    fields.String(
        attribute=lambda x: x.content[:100] if x.content
        else 'There was something error happend'
    ),
    'raw_content':
    fields.String(
        attribute=lambda x: x.raw_content[:150] if
        (x.raw_content and len(x.raw_content) > 100)
        else 'There was something error happend'
    ),
    'date':
    fields.String(attribute=lambda x: x.create_time.strftime('%Y-%m-%d')),
    'slug':
    fields.String
}

category_article_fields = {
    'slug': fields.String,
    'title': fields.String,
    'date':
    fields.String(attribute=lambda x: x.create_time.strftime('%Y-%m-%d'))
}

categories_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'articles': fields.Nested(category_article_fields)
}

mega_article_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'slug': fields.String,
    'content': fields.String,
    'raw_content': fields.String,
    'date':
    fields.String(attribute=lambda x: x.create_time.strftime('%Y-%m-%d'))
}

mega_some_fields = {'id': fields.Integer, 'name': fields.String}
