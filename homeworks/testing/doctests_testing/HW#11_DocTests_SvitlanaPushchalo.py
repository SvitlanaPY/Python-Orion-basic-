import doctest
from math import sqrt


class Calc:
    @staticmethod
    def sum(a, b):
        """
        Given two integers or floats, compute their sum.
        >>> Calc.sum(2, 3)
        5
        >>> Calc.sum(0.0, 1)
        1.0
        >>> Calc.sum('aaa', 5)
        Traceback (most recent call last):
            ...
        TypeError: can only concatenate str (not "int") to str

        :param a: first value, int/float
        :param b: second value, int/float
        :return: sum of values, int/float/Exception
        """
        return a + b

    @staticmethod
    def minus(a, b):
        """
        Given two integers or floats, compute their subtraction.
        >>> Calc.minus(0, 10)
        -10
        >>> Calc.minus(100, 50.0)
        50.0
        >>> Calc.minus(5, 'aaa')
        Traceback (most recent call last):
            ...
        TypeError: unsupported operand type(s) for -: 'int' and 'str'

        :param a: first value, int/float
        :param b: second value, int/float
        :return: subtraction of values, int/float/Exception
        """
        return a - b

    @staticmethod
    def mul(a, b):
        """
        Given two integers or floats, compute their multiplication.
        >>> Calc.mul(-5, 5)
        -25
        >>> Calc.mul(5, 10.0)
        50.0
        >>> Calc.mul('aaa', 2)
        TypeError('Invalid input, enter some number')

        :param a: first value, int/float
        :param b: second value, int/float
        :return: multiplication of values, int/float/Exception
        """
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a * b
        else:
            return TypeError('Invalid input, enter some number')

    @staticmethod
    def div(a, b) -> float:
        """
        Given two integers or floats, compute their division.
        >>> Calc.div(0.0, 5)
        0.0
        >>> Calc.div(10, 7)
        1.43
        >>> Calc.div(2, 'aaa') # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
            ...
        TypeError: BLA-BLA-BLA-BLA-BLA
        >>> Calc.div(10, 0)
        Traceback (most recent call last):
            ...
        ZeroDivisionError: division by zero

        :param a: first value, int/float
        :param b: second value, int/float
        :return: division of values, float/Exception
        """
        return round((a / b), 2)

    @staticmethod
    def pow(a, b):
        """
        Given two integers or floats, rise a-number to the b-power.
        >>> Calc.pow(0.0, 0)
        1.0
        >>> Calc.pow(0.0, 1)
        0.0
        >>> Calc.pow(-5, 11)
        -48828125
        >>> Calc.pow(2, 'aaa')
        Traceback (most recent call last):
            ...
        TypeError: unsupported operand type(s) for ** or pow(): 'int' and 'str'

        :param a: value, int/float
        :param b: power, int/float
        :return: rise any number to the power, int/float/Exception
        """
        return a ** b

    @staticmethod
    def root(a) -> float:
        """
         Given integer or float, compute the root of a number.
        >>> Calc.root(625.0)
        25.0
        >>> Calc.root(25)
        5.0
        >>> Calc.root(-25)
        Traceback (most recent call last):
            ...
        ValueError: math domain error
        >>> Calc.root('aaa')
        Traceback (most recent call last):
            ...
        TypeError: must be real number, not str

        :param a: value, int/float
        :return: square root of any number, float
        """
        return sqrt(a)

    @staticmethod
    def perc(a, b) -> float:
        """
        Given two integers or floats, compute 'a' percentage from 'b'.
        >>> Calc.perc(35, 500)
        175.0
        >>> Calc.perc(0, 10) # doctest: +SKIP
        0.0
        >>> Calc.perc('aaa', 100)
        Traceback (most recent call last):
            ...
        TypeError: unsupported operand type(s) for /: 'str' and 'int'

        :param a: percent, int/float
        :param b: value, int/float
        :return: percentage of any number, float/Exception
        """
        return (a * b) / 100


if __name__ == '__main__':
    doctest.testmode()

