from blog.main import m
from flask import jsonify, request, current_app
from blog.models import Article, Category, Tag
from datetime import datetime
from extand import db


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
        {'date': article.create_time.strftime('%Y-%m-%d'), 'title': article.title,
         'content': article.content[:100] + '...'} for article in pagination.items]
    return jsonify({'articles': articles})


@m.route('/article', methods=['GET', 'PUT'])
def get_article():
    if request.method == 'GET':
        title = request.args.get('title')
        if title:
            article = Article.query.filter_by(title=title).first()
            return jsonify(
                {'article': {'title': article.title, 'content': article.content,
                             'category': article.category.name if article.category else '',
                             'date': article.create_time.strftime('%Y-%m-%d'), 'id': article.id}})

    elif request.method == 'PUT':
        id = request.json['id']
        if id:
            article = Article.query.get(id)
            # article.title = request.json['data']['title']
            article.content = request.json['data']
            article.update_time = datetime.now()
            db.session.add(article)
            db.session.commit()
            return jsonify({'msg': 'success', 'status_code': 200})
        else:
            return jsonify({{'msg': 'not found', 'status_code': 404}})
    else:
        return jsonify({'article': 'error'})


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
                    for article in category.article]} for category in Category.query.all()]
    return jsonify({"category_json": category_json})


@m.route('/manage')
def manage():
    categories = [{'name': category.name, 'id': category.id, 'date': category.create_time.strftime('%Y-%m-%d')} for
                  category in Category.query.all()]
    articles = [
        {'id': article.id, 'title': article.title, 'category': article.category.name if article.category else '',
         'date': article.create_time.strftime('%Y-%m-%d')} for article in Article.query.all()]
    return jsonify({'manage': {'categories': categories, 'articles': articles}})


@m.route('/article_titles')
def get_article_titles():
    articles = [{'id': article.id, 'title': article.title} for article in Article.query.all()]
    return jsonify({'articles': articles})


@m.route('/category_titles')
def get_category_titles():
    categories = [{'id': category.id, 'name': category.name} for category in Category.query.all()]
    return jsonify({'categories': categories})


@m.route('/tag_titles')
def get_tag_titles():
    tags = [{'id': tag.id, 'name': tag.name} for tag in Tag.query.all()]
    return jsonify({'tags': tags})


@m.route('/new_article')
def new_article():
    pass


@m.route('/new_tag')
def new_tag():
    pass


@m.route('/do_test')
def add_items():
    for i in range(100):
        article = Article()
        article.title = 'for flask test ' + str(i)
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
