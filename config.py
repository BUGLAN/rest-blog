import os


class BaseConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@localhost:3306/restblog?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PAGE_ITEMS = 10
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'dist', 'static', 'images')
    SECRET_KEY = 'you will never guess me'
    RESTFUL_JSON = dict(ensure_ascii=False)


class TestConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
        os.path.abspath('.'), 'tests/test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PAGE_ITEMS = 10
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'dist', 'static', 'images')
    SECRET_KEY = 'you will never guess me'
    RESTFUL_JSON = dict(ensure_ascii=False)
