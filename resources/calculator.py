from calculator.simple import SimpleCalculator
from flask_restplus import Resource


class Calculator(Resource):
    def get(self, calculator_input):
        """
        Take an input string and calculate its result with a simple calculator.
        The input should contain spaces between numbers and operators.
        """
        calculator = SimpleCalculator()
        calculator.run(calculator_input)

        return {'result_of_calculation': calculator.reg_1}
