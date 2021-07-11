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
