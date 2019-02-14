from flask import Flask
from flask_restful import Api

from local_settings import HOST, PORT
from resources.calculator import Calculator

app = Flask(__name__)

api = Api(app)

api.add_resource(
    Calculator,
    '/calculator/<string:calculator_input>',
    endpoint='calculator',
)


if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)
