class CalcMath:
    """This class contains all the math related functions of a calculator"""

    def __init__(self):
        return
    
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
            return "error can not divide by 0"
        return float(numerator) / float(denominator)

    def exponentiation(self, base, exponent):
        """base ^ exponent"""
        return base ** exponent
    
    def square_root(self, radicand):
        """Returns the square root of the variable"""
        return radicand ** (1.0/2.0)
    
    def nth_root(self, radicand, degree):
        """radicand ^ (1 / degree)"""
        return radicand ** (1.0 / degree)
