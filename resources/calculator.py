from calculator.simple import SimpleCalculator
from flask_restplus import Resource


class Calculator(Resource):
    def get(self, calculator_input):
        """
        Take an input string and calculate its result with a simple calculator
        """
        calculator = SimpleCalculator()
        calculator.run(calculator_input)
        result_of_calculation = calculator.reg_1

        return result_of_calculation
