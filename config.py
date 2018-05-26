import os


class BaseConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@127.0.0.1:3306/restblog?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PAGE_ITEMS = 10
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'dist', 'static', 'images')
    SECRET_KEY = 'you will never guess me'
    RESTFUL_JSON = dict(ensure_ascii=False)
    HOST = 'http://127.0.0.1:5000'

class ProConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/restblog?charset=utf8'
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


config = {
        'dev': BaseConfig,
        'pro': ProConfig,
        'test': TestConfig
        }
