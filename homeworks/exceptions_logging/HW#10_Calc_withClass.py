class Calc:
    def __init__(self, val1, math_operation, val2):
        self.val1 = val1
        self.math_operation = math_operation
        self.val2 = val2

    def add(self):
        summ = self.val1 + self.val2
        return summ

    def subtract(self):
        subtrr = self.val1 - self.val2
        return subtrr

    def multiply(self):
        # multt = self.val1 * self.val2
        # return multt
        return self.val1 * self.val2

    def divide(self):
        try:
            divv = self.val1 / self.val2
        except ZeroDivisionError:
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
                print(f'Invalid input, it must be number')
                continue
            s = input("Choose math operation: (+, -, *, **, /, %, 'root'): ")
            if s not in ('+', '-', '*', '**', '/', 'root', '%'):
                continue
            try:
                self.val2 = float(input("Enter val2: "))
            except ValueError:
                print(f'Invalid input, enter some number')
                continue

            if s == '+':
                print(self.add())

            elif s == '-':
                print(self.subtract())

            elif s == '*':
                print(self.multiply())

            elif s == '/':
                print(self.divide())

            # elif s == 'root':
            #     print(self.root())

            elif s == 'root':
                try:
                    print(root())
                except:
                    print("Impossible to find the root from negative number")

            elif s == '**':
                print(self.power())

            elif s == '%':
                print(self.percentage())


obj = Calc(1, '+', 1)
obj.logic()




