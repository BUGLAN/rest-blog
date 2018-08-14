from blog import create_app
from blog.models import Article
from extand import db
import markdown

app = create_app('dev')


def do():
    with app.app_context():
        articles = Article.query.all()
        for article in articles:
            article.raw_content = article.content
            article.content = markdown.markdown(
                article.raw_content,
                extensions=[
                    'markdown.extensions.extra',
                    'markdown.extensions.codehilite',
                    'markdown.extensions.toc',
                ])
            db.session.add(article)
        db.session.commit()
    print('finish')


if __name__ == "__main__":
    do()
