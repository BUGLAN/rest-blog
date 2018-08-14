from flask import Flask
from extand import db
from flask_cors import CORS
from config import config


def create_app(config_name):
    app = Flask(
        __name__, static_folder='../dist/static', template_folder='../dist')
    db.init_app(app)
    CORS(app)
    # 相关配置
    app.config.from_object(config[config_name])
    # 相关路由
    #  from blog.main.views import m
    #  app.register_blueprint(m, url_prefix='/api')
    from blog.api.urls import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
