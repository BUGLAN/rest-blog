from blog.main import m
from flask import jsonify


@m.route('/api/articles')
def get_articles():
    return jsonify({'msg': 'success'})
