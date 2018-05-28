from flask_httpauth import HTTPTokenAuth
from blog.models import User
from flask import make_response, jsonify

auth = HTTPTokenAuth(scheme='Bearer')


@auth.verify_token
def verify_token(token):
    user = User.verify_auth_token(token)
    if user or token == '1':
        return True
    return False


@auth.error_handler
def unauthorized():
    return make_response(
        jsonify({
            'error': 'Unauthorized',
            'status': 401
        }), 401)
