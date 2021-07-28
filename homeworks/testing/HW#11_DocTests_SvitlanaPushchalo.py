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

        :param a: (int, float)
        :param b: (int, float)
        :return: (int, float)
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
        >>> Calc.minus('aaa', 5)
        Traceback (most recent call last):
            ...
        TypeError: unsupported operand type(s) for -: 'str' and 'int'

        :param a: (int, float)
        :param b: (int, float)
        :return: (int, float)
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

        :param a: (int, float)
        :param b: (int, float)
        :return: (int, float)
        """
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a * b
        else:
            return TypeError('Invalid input, enter some number')

    @staticmethod
    def div(a, b):
        """
        Given two integers or floats, compute their division.
        >>> Calc.div(0.0, 5)
        0.0
        >>> Calc.div(10, 7)
        1.43
        >>> Calc.div('aaa', 2)
        Traceback (most recent call last):
            ...
        TypeError: unsupported operand type(s) for /: 'str' and 'int'
        >>> Calc.div(10, 0)
        Traceback (most recent call last):
            ...
        ZeroDivisionError: division by zero

        :param a: (int, float)
        :param b: (int, float)
        :return: float
        """
        return round((a / b), 2)

    @staticmethod
    def pow(a, b):
        """
        Given two integers or floats, compute the power of a number.
        >>> Calc.pow(0.0, 0)
        1.0
        >>> Calc.pow(0.0, 1)
        0.0
        >>> Calc.pow(-5, 11)
        -48828125
        >>> Calc.pow('aaa', 2)
        Traceback (most recent call last):
            ...
        TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

        :param a: (int, float)
        :param b: (int, float)
        :return: (int, float)
        """
        return a ** b

    @staticmethod
    def root(a):
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

        :param a: (int, float)
        :return: float
        """
        return sqrt(a)

    @staticmethod
    def perc(a, b):
        """
        Given two integers or floats, compute 'a' percentage from 'b'.
        >>> Calc.perc(35, 500)
        175.0
        >>> Calc.perc(0, 10)
        0.0
        >>> Calc.perc('aaa', 100)
        Traceback (most recent call last):
            ...
        TypeError: unsupported operand type(s) for /: 'str' and 'int'

        :param a:(int, float)
        :param b:(int, float)
        :return: float
        """
        return (a * b) / 100

# In PyCharm in Terminal run the following command: $ python3 -m doctest -v HW#11_DocTests_SvitlanaPushchalo.py
