import os

env = os.getenv('ENV')
if env == 'production':
    USERNAME = os.getenv('USERNAME') or 'root'
    PASSWORD = os.getenv('PASSWORD') or 'root'
    HOST = os.getenv('HOST') or 'mysql'
    PORT = os.getenv('PORT') or 3306
    DATABASE = os.getenv('DATABASE') or 'rest'
else:
    USERNAME = os.getenv('USERNAME') or 'root'
    PASSWORD = os.getenv('PASSWORD') or 'root'
    HOST = '127.0.0.1'
    PORT = os.getenv('PORT') or 3306
    DATABASE = os.getenv('DATABASE') or 'rest'


class BaseConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}: \
            {}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOST, PORT,
                                       DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PAGE_ITEMS = 10
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'dist', 'static', 'images')
    SECRET_KEY = 'you will never guess me'
    RESTFUL_JSON = dict(ensure_ascii=False)
    HOST = 'http://127.0.0.1:5000'


class ProConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}: \
            {}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOST, PORT,
                                       DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PAGE_ITEMS = 10
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'dist', 'static', 'images')
    SECRET_KEY = 'you will never guess me'
    RESTFUL_JSON = dict(ensure_ascii=False)
    HOST = 'https://buglan.org'


class TestConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
        os.path.abspath('.'), 'tests/test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PAGE_ITEMS = 10
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'dist', 'static', 'images')
    SECRET_KEY = 'you will never guess me'
    RESTFUL_JSON = dict(ensure_ascii=False)


config = {'dev': BaseConfig, 'pro': ProConfig, 'test': TestConfig}
