from blog.main import m
from flask import jsonify, request, current_app
from blog.models import Article


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


@m.route('/article')
def get_article():
    title = request.args.get('title')
    if title:
        article = Article.query.filter_by(title=title).first()
        return jsonify({'article': {'title': article.title, 'content': article.content,
                                    'date': article.create_time.strftime('%Y-%m-%d')}})
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


from extand import db


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
