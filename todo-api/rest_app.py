# encoding: utf-8
#!/usr/bin/env python
'''
pip install flask-restful
'''
from flask import Flask
from flask_restful import Resource, Api, reqparse
from collections import OrderedDict

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('rate', type=int, help='Rate cannot be converted')
parser.add_argument('name', type=str)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
    def put(self):
        args = parser.parse_args()
        return {'todos': args['task']}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
