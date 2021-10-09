from flask import Flask, jsonify
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)

@api.route('/')
class HelloWorld(Resource):
    def get(self):
        return {'message':'hello world'}


if __name__ == '__main__':
    app.run(debug=True)
