from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)


class Todo(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
                'id',
                type=int
                )
        args = parser.parse_args()
        id = args['id']
        return id

api.add_resource(Todo, '/todo')


if __name__ == '__main__':
    app.run(debug=True)
