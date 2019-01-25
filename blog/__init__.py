import os

from flask import Flask, render_template

import pymysql
from config import HOST, PASSWORD, USERNAME, config
from extand import db
from flask_cors import CORS


def init_db():
    # create database if not exits && create all the table
    conn = pymysql.connect(host=HOST, user=USERNAME, password=PASSWORD)
    conn.cursor().execute('CREATE DATABASE IF NOT EXISTS rest')
    conn.close()
    db.create_all()


def create_app(config_name):

    app = Flask(
        __name__,
        static_url_path='',
        static_folder=os.path.abspath('./rest/dist/'),
        template_folder=os.path.abspath('./rest/dist/'))
    app.config.from_object(config[config_name])
    db.init_app(app)
    CORS(app)

    app.before_first_request(init_db)

    @app.route('/test')
    def test():
        return render_template('index.html')

    # 相关配置 相关路由
    #  from blog.main.views import m
    #  app.register_blueprint(m, url_prefix='/api')
    from blog.api.urls import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
