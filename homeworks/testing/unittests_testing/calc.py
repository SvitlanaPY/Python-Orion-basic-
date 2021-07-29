from math import sqrt

class Calc:
    @staticmethod
    def sum(a, b):
        return a + b

    @staticmethod
    def minus(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        return round((a / b), 2)

    @staticmethod
    def pow(a, b):
        return a ** b

    @staticmethod
    def root(a):
        return sqrt(a)

    @staticmethod
    def perc(a, b):
        return (a * b) / 100