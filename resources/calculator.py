# from calculator.simple import SimpleCalculator
# from flask import Blueprint
# from flask_restful import Resource, Api
from flask_restplus import Resource # , Api


class Calculator(Resource):
    def get(self):
        return 'Test'


# calculator_api = Blueprint(name='resources.calculator', import_name=__name__)
# api = Api(calculator_api)
# api.add_resource(
#     resource=Calculator,
#     urls='/calculator',
#     # endpoint='calculator',
# )
#
# print(api)
# print(dir(calculator_api))
# print(calculator_api.__dict__)
# print(api.__dict__)
