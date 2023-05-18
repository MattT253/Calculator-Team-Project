class CalcMath:
    """This class contains all the math related functions of a calculator"""

    def __init__(self):
        self.operations = {'+': 'addition', '-': 'subtraction', '÷': 'division',
                           'X': 'multiplication', 'a'u'\u02E3': 'exponentiation',
                           '√': 'square_root', 'a√x': 'nth_root', '±': 'negation'}
        return
    
    def calculate(self, operator, num1, num2=''):
        operator = self.operations[operator]

        if num2 == '':
            result = eval('self.%s(%s)' % (operator, num1))
        else:
            result = eval('self.%s(%s,%s)' % (operator, num1, num2))

        # Check if the result is a float datatype, then use the float.is_integer() method
        #   to check if the result has no fractional part. If true, cast to an int and return
        if isinstance(result, float):
            if result.is_integer():
                return int(result)
        return result

    def addition(self, augend, addend):
        """augend + addend"""
        return augend + addend
    
    def subtraction(self, minuend, subtrahend):
        """minuend - subtrahend"""
        return minuend - subtrahend

    def multiplication(self, multiplier, multiplicand):
        """multipler * multipicand"""
        return multiplier * multiplicand

    def division(self, numerator, denominator):
        """numerator / denominator"""
        # Check if the denominator is 0
        if denominator == 0:
            return "Error: can not divide by 0"
        return float(numerator) / float(denominator)
    
    def negation(self, value):
        """value * -1"""
        return value * -1

    def exponentiation(self, base, exponent):
        """base ^ exponent"""
        return base ** exponent
    
    def square_root(self, radicand):
        """Returns the square root of the variable"""
        return radicand ** (1.0/2.0)
    
    def nth_root(self, degree, radicand):
        """radicand ^ (1 / degree)"""
        return radicand ** (1.0 / degree)
