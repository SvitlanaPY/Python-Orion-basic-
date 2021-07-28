import logging

logging.basicConfig(filename="Calc_logs.log", level=logging.INFO, filemode='a')


class Calc:
    def __init__(self, val1=0, math_operation='', val2=0):
        self.val1 = val1
        self.math_operation = math_operation
        self.val2 = val2

    def add(self):
        return self.val1 + self.val2

    def subtract(self):
        subtrr = self.val1 - self.val2
        return subtrr

    def multiply(self):
        multt = self.val1 * self.val2
        return multt

    def divide(self):
        try:
            divv = self.val1 / self.val2
        except ZeroDivisionError:
            logging.error('Division by zero performed!')
            return "Division by zero!"
        else:
            return divv

    # def root(self):
    #     roott = self.val1 ** (1 / self.val2)
    #     return roott

    def root(self):
        if self.val1 > 0:
            roott = self.val1 ** (1 / self.val2)
            return roott
        else:
            raise Exception

    def power(self):
        poww = self.val1 ** self.val2
        return poww

    def percentage(self):
        percc = self.val1 * self.val2 / 100
        return percc

    def logic(self):
        while True:
            try:
                self.val1 = float(input("Enter val1: "))
            except ValueError:
                print('Invalid input, it must be number')
                logging.error("ERROR: Invalid input for val1")
                continue
            s = input("Choose math operation: (+, -, *, **, /, %, 'root'): ")
            if s not in ('+', '-', '*', '**', '/', 'root', '%'):
                continue
            try:
                self.val2 = float(input("Enter val2: "))
            except ValueError:
                print('Invalid input, enter some number')
                logging.error('Invalid input for val2')
                continue

            if s == '+':
                print(self.add())
                logging.info("Math operation '+' is performed")

            elif s == '-':
                print(self.subtract())
                logging.info("Math operation '-' is performed")

            elif s == '*':
                print(self.multiply())
                logging.info("Math operation '*' is performed")

            elif s == '/':
                print(self.divide())
                logging.info("Math operation '/' is performed")

            # elif s == 'root':
            #     print(self.root())

            elif s == 'root':
                try:
                    print(self.root())
                    logging.info("Math operation 'root' is performed")
                except:
                    print("Impossible to find the root from negative number")
                    logging.error('Root from negative number')

            elif s == '**':
                print(self.power())
                logging.info("Math operation '**' is performed")

            elif s == '%':
                print(self.percentage())
                logging.info("Math operation '%' is performed")


obj = Calc()
obj.logic()
