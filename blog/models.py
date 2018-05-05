from extand import db
from datetime import datetime


class Article(db.Model):
    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=True)
    content = db.Column(db.Text)
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)

    def __init__(self):
        super(Article, self).__init__()
        self.create_time = datetime.now()
        self.update_time = datetime.now()

    def __repr__(self):
        return '<Article %r> at %r' % (self.title, self.create_time)