from flask import Flask
from flask_cors import CORS

from config import config
from extand import db
import pymysql


def init_db():
    # create database if not exits && create all the table
    conn = pymysql.connect(host='127.0.0.1', user='root', password='root')
    conn.cursor().execute('CREATE DATABASE IF NOT EXISTS rest')
    conn.close()
    db.create_all()


def create_app(config_name):

    app = Flask(
        __name__, static_folder='../dist/static', template_folder='../dist')
    app.config.from_object(config[config_name])
    db.init_app(app)
    CORS(app)

    app.before_first_request(init_db)

    # 相关配置 相关路由
    #  from blog.main.views import m
    #  app.register_blueprint(m, url_prefix='/api')
    from blog.api.urls import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
