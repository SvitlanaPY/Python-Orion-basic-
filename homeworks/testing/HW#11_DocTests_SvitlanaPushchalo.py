class Calc:
    @staticmethod
    def sum(a, b):
        """
        Given two integers or floats, compute their sum.
        >>> Calc.sum(2, 3)
        5
        >>> Calc.sum(0.0, 1)
        1.0
        >>> Calc.sum('a', 5)
        ValueError('Invalid input, enter some number')

        :param a: (int, float)
        :param b: (int, float)
        :return: (int, float)
        """
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b
        else:
            return ValueError('Invalid input, enter some number')

    @staticmethod
    def minus(a, b):
        """
        Given two integers or floats, compute their subtraction.
        >>> Calc.minus(0, 10)
        -10
        >>> Calc.minus(100, 50.0)
        50.0
        >>> Calc.minus('b', 5)
        ValueError('Invalid input, enter some number')

        :param a: (int, float)
        :param b: (int, float)
        :return: (int, float)
        """
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a - b
        else:
            return ValueError('Invalid input, enter some number')

    @staticmethod
    def mul(a, b):
        """
        Given two integers or floats, compute their multiplication.
        >>> Calc.mul(-5, 5)
        -25
        >>> Calc.mul(5, 10.0)
        50.0
        >>> Calc.mul('c', 2)
        ValueError('Invalid input, enter some number')

        :param a: (int, float)
        :param b: (int, float)
        :return: (int, float)
        """
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a * b
        else:
            return ValueError('Invalid input, enter some number')

    @staticmethod
    def div(a, b):
        """
        Given two integers or floats, compute their division.
        >>> Calc.div(0.0, 5)
        0.0
        >>> Calc.div(10, 7)
        1.43
        >>> Calc.div('div', 2)
        ValueError('Invalid input, enter some number')
        >>> Calc.div(10, 0)
        ZeroDivisionError('Divisor is zero!')

        :param a: (int, float)
        :param b: (int, float)
        :return: float
        """
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            if b != 0:
                return round((a / b), 2)
            else:
                return ZeroDivisionError("Divisor is zero!")
        else:
            return ValueError('Invalid input, enter some number')

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
        >>> Calc.pow('pow', 2)
        ValueError('Invalid input, enter some number')

        :param a: (int, float)
        :param b: (int, float)
        :return: (int, float)
        """
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a ** b
        else:
            return ValueError('Invalid input, enter some number')

    @staticmethod
    def root(a, b):
        """
        Given two integers or floats, compute the root of a number.
        >>> Calc.root(125.0, 3)
        5.0
        >>> Calc.root(255, 2)
        15.97
        >>> Calc.root(-625, 4)
        ValueError('Impossible to find the root from negative number')
        >>> Calc.root('root', 2)
        ValueError('Invalid input, enter some number')

        :param a: (int, float)
        :param b: (int, float)
        :return: float
        """
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            if a > 0:
                return round((a ** (1 / b)), 2)
            else:
                return ValueError('Impossible to find the root from negative number')
        else:
            return ValueError('Invalid input, enter some number')

    @staticmethod
    def perc(a, b):
        """
        Given two integers or floats, compute 'a' percentage from 'b'.
        >>> Calc.perc(35, 500)
        175.0
        >>> Calc.perc(0, 10)
        0.0
        >>> Calc.perc('perc', 25)
        ValueError('Invalid input, enter some number')

        :param a:(int, float)
        :param b:(int, float)
        :return: float
        """
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a * b / 100
        else:
            return ValueError('Invalid input, enter some number')

# In PyCharm in Terminal run the following command: $ python3 -m doctest -v HW#11_DocTests_SvitlanaPushchalo.py
