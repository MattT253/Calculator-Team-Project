import math

class CalcMath:
    """This class contains all the math related functions of a calculator"""

    def __init__(self):
        self.operations = {'+': 'addition', '-': 'subtraction', '÷': 'division',
                           'X': 'multiplication', 'a'u'\u02E3': 'exponentiation',
                           '√': 'square_root', 'a√x': 'nth_root', '±': 'negation',
                            'log': 'logarithm', 'mod': 'modulo'}
        return
    
    def calculate(self, operator, num1, num2=''):
     operator = self.operations[operator]
     method = getattr(self, operator)

     if num2 == '':
        result = method(float(num1))
     else:
        result = method(float(num1), float(num2))

     if isinstance(result, float) and result.is_integer():
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
    
    def logarithm(self, base, number):
        """Returns the logarithm of a number"""
        return math.log(number, base)
    
    def modulo(self, dividend, divisor):
        """Returns the remainder of the division"""
        return dividend % divisor