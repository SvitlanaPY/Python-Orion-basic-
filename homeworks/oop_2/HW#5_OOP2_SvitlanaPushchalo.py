print('########## 1 ##########')
# class Laptop:
#     """
#     Make the class with composition.
#     """
# class Battery:
#     """
#     Make the class with composition.
#     """

class Laptop:  # container
    def __init__(self):
        bt = Battery(50)
        self.battery = bt

class Battery:
    def __init__(self, charge_level=100):
        self.charge_level = charge_level

laptop = Laptop()
print(laptop.battery)
# OUTPUT: <__main__.Battery object at 0x7f398edc8d60>


print('\n########## 2 ##########')
# class Guitar:
#     """
#     Make the class with aggregation
#     """
# class GuitarString:
#     """
#     Make the class with aggregation
#     """

class Guitar:
    def __init__(self, string):
        self.string = string
        print('Hi')

class GuitarString:
    def __init__(self):
        pass

gs = GuitarString()
guitar = Guitar(gs)
print(guitar.string)
# OUTPUT: <__main__.GuitarString object at 0x7f398ed32070>


print('\n########## 3 ##########')
# class Calc:
#     """
#     Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
#     Note: this method should be static
#     """

class Calc:

    @staticmethod
    def add_nums(a, b, c):
        summa = a + b + c
        return summa

addnums = Calc()
print(addnums.add_nums(1, 2, 3))
# OUTPUT: 6
print(Calc.add_nums(1, 2, 3))
# OUTPUT: 6


print('\n########## 4* ##########')
# class Pasta:
#     """
#     Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
#     It should have 2 methods:
#     carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
#     which should create Pasta instances with predefined list of ingredients.
#     Example:
#         pasta_1 = Pasta(["tomato", "cucumber"])
#         pasta_1.ingredients will equal to ["tomato", "cucumber"]
#         pasta_2 = Pasta.bolognaise()
#         pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
#     """

class Pizza:
    def __init__(self, ingredients = []):
        self.ingredients = ingredients

    @classmethod
    def carbonara (cls):
        return Pizza(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise (cls):
        return Pizza(['bacon', 'parmesan', 'eggs'])

pizza_carbonara = Pizza.carbonara()
print('pizza_carbonara:', pizza_carbonara.ingredients)
pizza_bolognaise = Pizza.bolognaise()
print('pizza_bolognaise:', pizza_bolognaise.ingredients)
