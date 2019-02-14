from flask import Flask
from flask_restful import Api

from local_settings import HOST, PORT
from resources.calculator import Calculator  # , calculator_api

app = Flask(__name__)

api = Api(app)

api.add_resource(Calculator, '/calculator')
# app.register_blueprint(calculator_api)


# NOG IETS DOEN MET reqparse? om te kijken of arguments valide zijn!?!
# @app.route('/calculator/<string:calculator_input>', methods=['GET'])
# def calculate(calculator_input):
#     """
#     Take an input string and calculate its result with a simple calculator
#     """
#     print(calculator_input)
#     calculator = SimpleCalculator()
#     calculator.run(calculator_input)
#     print(calculator.log)
#     result = calculator.reg_1
#
#     return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)
