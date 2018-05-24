"""
my rest-blog api
author buglan
"""

import os
import sqlalchemy
from datetime import datetime

from flask import jsonify, request, current_app, make_response, abort

from blog.main import m
from blog.models import Article, Category, Tag, User
from extand import db
from sqlalchemy import and_
from flask_httpauth import HTTPTokenAuth

auth = HTTPTokenAuth(scheme='Bearer')


@auth.verify_token
def verify_token(token):
    user = User.verify_auth_token(token)
    if user:
        return True
    return False


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized'}), 401)


@m.route('/articles')
def get_articles():
    page = request.args.get('page') or 1
    if not isinstance(page, int):
        abort(404)
    items = current_app.config['PAGE_ITEMS']
    pagination = Article.query.order_by(Article.create_time.desc()).paginate(
        int(page), items, error_out=False)
    """
    required: page = 1
    return to: {"articles": [
            {"date": '2018-2-2', "title": "title", "content": "content"}]}
    """
    articles = [{
        'date': article.create_time.strftime('%Y-%m-%d'),
        'title': article.title,
        'slug': article.slug,
        'content': article.content[:100] + '...'
    } for article in pagination.items]
    return jsonify({'articles': articles})


@m.route('/article', methods=['GET'])
def get_article():
    slug = request.args.get('slug')
    if slug:
        article = Article.query.filter_by(slug=slug).first()
        if article:
            return jsonify({
                'article': {
                    'title': article.title,
                    'content': article.content,
                    'slug': article.slug,
                    'date': article.create_time.strftime('%Y-%m-%d'),
                    'id': article.id,
                    'category': {
                        'id': article.category.id,
                        'name': article.category.name
                    } if article.category else '',
                    'tags': {
                        'id': [tag.id for tag in article.tags],
                        'name': [tag.name for tag in article.tags]
                    }
                }
            })
        abort(404)
    else:
        abort(400)


@m.route('/article_operation', methods=['PUT', 'DELETE'])
def article_operation():
    if request.method == 'PUT':
        try:
            id = request.json.get('id')
        except AttributeError:
            return jsonify({'msg': 'fail', 'status_code': 400})
        if isinstance(id, int):
            article = Article.query.get(id)
            article.title = request.json.get('title')
            article.slug = request.json.get('slug')
            article.content = request.json['content']
            article.update_time = datetime.now()
            category_id = request.json.get('category')
            if category_id and isinstance(category_id, int):
                article.category = Category.query.get_or_404(category_id)
            article.tags = [
                Tag.query.get(tag_id) for tag_id in request.json.get('tags')
            ]
            article.update_time = datetime.now()
            db.session.add(article)
            db.session.commit()
            return jsonify({'msg': 'success', 'status_code': 200})
        else:
            return jsonify({{'msg': 'not found', 'status_code': 404}})
    elif request.method == 'DELETE':
        try:
            id = request.args.get('id')
        except AttributeError:
            abort(400)
        article = Article.query.get(id)
        db.session.delete(article)
        db.session.commit()
        return jsonify({'msg': 'success', 'status_code': 200})


@m.route('/pages')
def get_pages():
    pages = len(Article.query.all())
    items = current_app.config['PAGE_ITEMS']
    page_num = pages // items
    if pages % items > 0:
        page_num += 1
    return jsonify({'pages': [page for page in range(1, page_num + 1)]})


@m.route('/categories')
def get_categories():
    """
    {
        categories: [{"python": {title: "..."}}]
    }
    """
    category_json = [{
        'name':
        category.name,
        'titles': [{
            "name": article.title,
            'date': article.create_time.strftime('%Y-%m-%d')
        } for article in category.articles]
    } for category in Category.query.all()]
    return jsonify({"category_json": category_json})


@m.route('/manage')
@auth.login_required
def manage():
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
    return jsonify({
        'manage': {
            'categories': categories,
            'articles': articles,
            'tags': tags
        }
    })


@m.route('/article_titles')
@auth.login_required
def get_article_titles():
    articles = [{
        'id': article.id,
        'title': article.title
    } for article in Article.query.all()]
    return jsonify({'articles': articles})


@m.route('/category_titles')
@auth.login_required
def get_category_titles():
    categories = [{
        'id': category.id,
        'name': category.name
    } for category in Category.query.all()]
    return jsonify({'categories': categories})


@m.route('/tag_titles')
@auth.login_required
def get_tag_titles():
    """
    provide tag basic msg
    """
    tags = [{'id': tag.id, 'name': tag.name} for tag in Tag.query.all()]
    return jsonify({'tags': tags})


@m.route('/new_category', methods=['POST'])
@auth.login_required
def new_category():
    try:
        category = request.json.get('category')
        article_ids = request.json.get('articles')
    except AttributeError:
        abort(400)
    print(category)
    if category:
        try:
            articles = [Article.query.get(id) for id in article_ids]
        except BaseException:
            abort(400)
        try:
            c = Category()
            c.name = category
            c.articles = articles
            db.session.add(c)
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            return jsonify({'status': '400', 'msg': '分类名重复'}), 400
        return jsonify({'status': 200})
    return jsonify({'status': 404}), 404


@m.route('/new_tag', methods=['POST'])
@auth.login_required
def new_tag():
    try:
        tag = request.json.get('tag')
        article_ids = request.json.get('articles')
    except AttributeError:
        abort(400)
    if tag:
        articles = [Article.query.get(int(id)) for id in article_ids]
        try:
            t = Tag()
            t.name = tag
            t.articles = articles
            db.session.add(t)
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            return jsonify({'status': 400, 'msg': '标签名重复'}), 400
        return jsonify({'status': 200})
    return jsonify({'status': 404}), 404


@m.route('/new_article', methods=['POST'])
@auth.login_required
def new_article():
    try:
        title = request.json.get('title')
        slug = request.json.get('slug')
        category_id = request.json.get('category')
        tag_ids = request.json.get('tags')
        content = request.json.get('content')
    except AttributeError:
        abort(400)
    if title and content:
        article = Article()
        article.title = title
        article.slug = slug
        try:
            article.category = Category.query.get(category_id)
        except:
            pass
        article.tags = [Tag.query.get(int(id)) for id in tag_ids]
        article.content = content
        db.session.add(article)
        db.session.commit()
        return jsonify({'status': 200})
    return jsonify({'status': 404}), 404


@m.route('/upload_image', methods=['POST'])
@auth.login_required
def upload_image():
    try:
        file = request.files.get('image')
    except AttributeError:
        abort(400)
    if file and file.filename:
        if not os.path.exists(current_app.config['UPLOAD_FOLDER']):
            os.makedirs(current_app.config['UPLOAD_FOLDER'])
        file.save(
            os.path.join(current_app.config['UPLOAD_FOLDER'], file.filename))
        return jsonify({
            'url':
            'http://127.0.0.1:5000/' + 'static/' + 'images/' + file.filename,
            'status':
            200
        })
    else:
        return jsonify({'status': 400})


@m.route('/category_operation', methods=['GET', 'DELETE', 'PUT'])
def category_operation():
    if request.method == 'GET':
        name = request.args.get('name')
        category = Category.query.filter_by(name=name).first()
        if category:
            return jsonify({
                'category': {
                    'id': category.id,
                    'name': category.name
                }
            })
        else:
            return jsonify({'status': 404})
    elif request.method == 'DELETE':
        id = request.args.get('id')
        category = Category.query.get(id)
        db.session.delete(category)
        db.session.commit()
        return jsonify({'status': 200})

    elif request.method == 'PUT':
        name = request.json.get('name')
        id = request.json.get('id')
        category = Category.query.get(id)
        category.name = name
        category.update_time = datetime.now()
        db.session.add(category)
        db.session.commit()
        return jsonify({'status': 200})


@m.route('/tag_operation', methods=['GET', 'PUT', 'DELETE'])
def tag_operation():
    if request.method == 'GET':
        name = request.args.get('name')
        tag = Tag.query.filter_by(name=name).first()
        if tag:
            return jsonify({'tag': {'id': tag.id, 'name': tag.name}})
        else:
            return jsonify({'status': 404})

    elif request.method == 'PUT':
        name = request.json.get('name')
        id = request.json.get('id')
        tag = Tag.query.get(id)
        tag.name = name
        tag.update_time = datetime.now()
        db.session.add(tag)
        db.session.commit()
        return jsonify({'status': 200})

    elif request.method == 'DELETE':
        id = request.args.get('id')
        tag = Tag.query.get(id)
        db.session.delete(tag)
        db.session.commit()
        return jsonify({'status': 200})


@m.route('/login', methods=['POST'])
def login():
    try:
        username = request.json.get('username')
        password = request.json.get('password')
    except AttributeError:
        abort(400)
    user = User.query.filter(
        and_(User.password == password, User.name == username)).first()
    if user:
        token = user.generate_auth_token().decode('ascii')
        response = make_response(jsonify({'token': token}), 200)
        return response
    else:
        abort(400)


@m.route('/login_test')
@auth.login_required
def login_test():
    return jsonify({'msg': 'success'})
