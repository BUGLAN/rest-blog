from extand import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)

    def __init__(self):
        super(User, self).__init__()
        self.create_time = datetime.now()
        self.update_time = datetime.now()

    def __repr__(self):
        return '<User %r>' % self.name


article_tag = db.Table(
    'article_tag',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('article_id', db.Integer, db.ForeignKey('article.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
)


class Article(db.Model):
    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=True)
    content = db.Column(db.Text)
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    tags = db.relationship(
        'Tag',
        secondary=article_tag,
        backref=db.backref('articles', lazy='dynamic'),
        lazy='dynamic'
    )

    def __init__(self):
        super(Article, self).__init__()
        self.create_time = datetime.now()
        self.update_time = datetime.now()

    def __repr__(self):
        return '<Article %r> at %r' % (self.title, self.create_time)


class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(58), unique=True)
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    articles = db.relationship('Article', backref='category')

    def __init__(self):
        super(Category, self).__init__()
        self.create_time = datetime.now()
        self.update_time = datetime.now()

    def __repr__(self):
        return "<Category %r>" % self.name


class Tag(db.Model):
    __tablename__ = 'tag'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(58), unique=True)
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)

    def __init__(self):
        super(Tag, self).__init__()
        self.create_time = datetime.now()
        self.update_time = datetime.now()

    def __repr__(self):
        return '<Tag %r>' % self.name
