import os
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
    items = current_app.config['PAGE_ITEMS']
    pagination = Article.query.order_by(Article.create_time.desc()).paginate(int(page), items, error_out=False)
    """
    required: page = 1
    return to: {"articles": [
            {"date": '2018-2-2', "title": "title", "content": "content"}]}
    """
    articles = [
        {'date': article.create_time.strftime('%Y-%m-%d'), 'title': article.title, 'slug': article.slug,
         'content': article.content[:100] + '...'} for article in pagination.items]
    return jsonify({'articles': articles})


@m.route('/article', methods=['GET'])
def get_article():
    slug = request.args.get('slug')
    if slug:
        article = Article.query.filter_by(slug=slug).first()
        if article:
            return jsonify(
                {'article': {'title': article.title, 'content': article.content, 'slug': article.slug,
                             'date': article.create_time.strftime('%Y-%m-%d'), 'id': article.id,
                             'category': {'id': article.category.id,
                                          'name': article.category.name} if article.category else '',
                             'tags': {'id': [tag.id for tag in article.tags],
                                      'name': [tag.name for tag in article.tags]}
                             }})
        return jsonify({'status': 400}), 400


@m.route('/article_operation', methods=['PUT', 'DELETE'])
def article_operation():
    if request.method == 'PUT':
        id = request.json['id']
        if id:
            article = Article.query.get(id)
            article.title = request.json.get('title')
            article.slug = request.json.get('slug')
            article.content = request.json['content']
            article.update_time = datetime.now()
            category_id = request.json.get('category')
            if category_id and isinstance(category_id, int):
                article.category = Category.query.get_or_404(category_id)
            article.tags = [Tag.query.get(tag_id) for tag_id in request.json.get('tags')]
            article.update_time = datetime.now()
            db.session.add(article)
            db.session.commit()
            return jsonify({'msg': 'success', 'status_code': 200})
        else:
            return jsonify({{'msg': 'not found', 'status_code': 404}})
    elif request.method == 'DELETE':
        id = request.args.get('id')
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
    category_json = [
        {'name': category.name,
         'titles': [{"name": article.title, 'date': article.create_time.strftime('%Y-%m-%d')}
                    for article in category.articles]} for category in Category.query.all()]
    return jsonify({"category_json": category_json})


@m.route('/manage')
@auth.login_required
def manage():
    categories = [{'name': category.name, 'id': category.id, 'date': category.create_time.strftime('%Y-%m-%d')} for
                  category in Category.query.all()]
    articles = [
        {'id': article.id, 'title': article.title, 'slug': article.slug, 'category': article.category.name if article.category else '',
         'tags': [tag.name for tag in article.tags] if article.tags else [],
         'date': article.create_time.strftime('%Y-%m-%d')} for article in Article.query.all()]
    tags = [{'id': tag.id, 'name': tag.name, 'date': tag.create_time.strftime('%Y-%m-%d')} for tag in Tag.query.all()]
    return jsonify({'manage': {'categories': categories, 'articles': articles, 'tags': tags}})


@m.route('/article_titles')
@auth.login_required
def get_article_titles():
    articles = [{'id': article.id, 'title': article.title} for article in Article.query.all()]
    return jsonify({'articles': articles})


@m.route('/category_titles')
@auth.login_required
def get_category_titles():
    categories = [{'id': category.id, 'name': category.name} for category in Category.query.all()]
    return jsonify({'categories': categories})


@m.route('/tag_titles')
@auth.login_required
def get_tag_titles():
    tags = [{'id': tag.id, 'name': tag.name} for tag in Tag.query.all()]
    return jsonify({'tags': tags})


@m.route('/new_category', methods=['POST'])
@auth.login_required
def new_category():
    category = request.json.get('category')
    article_ids = request.json.get('articles')
    if category and article_ids:
        articles = [Article.query.get(int(id)) for id in article_ids]
        c = Category()
        c.name = category
        c.articles = articles
        db.session.add(c)
        db.session.commit()
        return jsonify({'status': 200})
    return jsonify({'status': 404}), 404


@m.route('/new_tag', methods=['POST'])
@auth.login_required
def new_tag():
    tag = request.json.get('tag')
    article_ids = request.json.get('articles')
    if tag and article_ids:
        articles = [Article.query.get(int(id)) for id in article_ids]
        t = Tag()
        t.name = tag
        t.articles = articles
        db.session.add(t)
        db.session.commit()
        return jsonify({'status': 200})
    return jsonify({'status': 404}), 404


@m.route('/new_article', methods=['POST'])
@auth.login_required
def new_article():
    title = request.json.get('title')
    slug = request.json.get('slug')
    category_id = request.json.get('category')
    tag_ids = request.json.get('tags')
    content = request.json.get('content')
    if title and content:
        article = Article()
        article.title = title
        article.slug = slug
        article.category = Category.query.get(int(category_id)) if Category.query.get(int(category_id)) else None
        article.tags = [Tag.query.get(int(id)) for id in tag_ids]
        article.content = content
        db.session.add(article)
        db.session.commit()
        return jsonify({'status': 200})
    return jsonify({'status': 404}), 404


@m.route('/upload_image', methods=['POST'])
@auth.login_required
def upload_image():
    file = request.files.get('image')
    if file and file.filename:
        if not os.path.exists(current_app.config['UPLOAD_FOLDER']):
            os.makedirs(current_app.config['UPLOAD_FOLDER'])
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], file.filename))
        return jsonify({'url': 'http://127.0.0.1:5000/' + 'static/' + 'images/' + file.filename, 'status': 200})
    else:
        return jsonify({'status': 400})


@m.route('/category_operation', methods=['GET', 'DELETE', 'PUT'])
def category_operation():
    if request.method == 'GET':
        name = request.args.get('name')
        category = Category.query.filter_by(name=name).first()
        if category:
            return jsonify({'category': {'id': category.id, 'name': category.name}})
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
    username = request.json.get('username')
    password = request.json.get('password')
    user = User.query.filter(and_(User.password == password, User.name == username)).first()
    if user:
        token = user.generate_auth_token().decode('ascii')
        response = make_response(jsonify({'token': token}), 200)
        # response.set_cookie(key='token', value=user.generate_auth_token().decode('ascii'), secure=False)
        return response
    else:
        abort(400)


@m.route('/login_test')
@auth.login_required
def login_test():
    print(request.cookies.get('token'))
    return jsonify({'msg': 'success'})


@m.route('/do_test')
def add_items():
    for i in range(100):
        article = Article()
        article.title = 'for flask test ' + str(i)
        article.slug = 'just-do-it-' + str(i)
        article.content = "东西不错，就是拿回来的时候吓了我一跳，我买的法拉利混光版的，然后给了我一个伯爵红的，我还以为没" \
                          "背光，后来试了一下原来是有背光的，买的樱桃红轴，手感很不错，不像黑轴按着那么累，可以好好的玩游戏了" \
                          "，卖家人很好，发消息都是秒回。唯一不爽的一点就是顺丰太慢了一个键盘发了3天，和普通快递差不多！总之东西非常不错，下次还会再来。"
        db.session.add(article)
        db.session.commit()
    return 'success'


@m.route('/do_add_categories')
def add_categories():
    for i in range(100):
        c = Category()
        c.name = 'rest blog category test ' + str(i)
        db.session.add(c)
        db.session.commit()
        a = Article()
        a.title = 'rest blog test ' + str(i)
        a.content = """查找问题之后，才明白，是因为Flask_admin保存对象时，调用的是默认的init方法，也就是说并没有往init的参数中赋值，而是在随后的处理中，进行赋值，就是先初始化，后赋值．那么我们重载的这个init方法，这几个参数都会被设置为None.而我们对create_time这种变量还进行了处理，如果去掉create_time这种字段，保存时不会出错，但是当从redis中获取到字符串并eval试图构建对象时，就会有各种问题．

        为了解决这个问题，有效的利用redis缓存带来的性能提升，找到了一个合适的方法解决这个问题，暂且称它为＂创建一个镜像类＂，也就是说创造一个跟这个model字段一模一样的类，只是不去继承SQLAlchemy的语义，定义如下："""
        a.category = c
        db.session.add(a)
        db.session.commit()
    return 'success'
