# 1. Create a Vehicle class with max_speed and mileage instance attributes
class Vehicle:
    def __init__(self, max_speed=0, mileage=0):
        self.max_speed = max_speed
        self.mileage = mileage

veh = Vehicle(10, 20)
print(veh.max_speed, veh.mileage)
# OUTPUT: 10 20

# 2. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class and will have seating_capacity own method
class Bus(Vehicle):
    def __init__(self, max_speed=0, mileage=0, seating_capacity=0):
        super().__init__(max_speed, mileage)
        self.seating_capacity = seating_capacity

bus = Bus(100, 200, 300)
print(bus.max_speed, bus.mileage, bus.seating_capacity)
# OUTPUT: 100 200 300

# 3. Determine which class a given Bus object belongs to (Check type of an object)
bus1 = Bus()
print(type(bus1))
# OUTPUT: <class '__main__.Bus'>
print(issubclass(Bus,Vehicle))
# OUTPUT: True
print(isinstance(bus1, Bus))
# OUTPUT: True
print(isinstance(bus1, Vehicle))
# OUTPUT: True

# 4. Determine if School_bus is also an instance of the Vehicle class
School_bus = Bus(10, 20, 30)
print(isinstance(School_bus, Vehicle))
# OUTPUT: True

# 5. Create a new class School with get_school_id and number_of_students instance attributes
class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students

sch = School(108, 450)
print(sch.get_school_id, sch.number_of_students)
# OUTPUT: 108 450

# 6*. Create a new class SchoolBus that will inherit all of the methods from School and Bus and will have its own - bus_school_color
# class Vehicle:
#     def __init__(self, max_speed=0, mileage=0):
#         self.max_speed = max_speed
#         self.mileage = mileage
# class School:
#     def __init__(self, get_school_id, number_of_students):
#         self.get_school_id = get_school_id
#         self.number_of_students = number_of_students
# class Bus(Vehicle):
#     def __init__(self, max_speed=0, mileage=0, seating_capacity=0):
#         super().__init__(max_speed, mileage)
#         self.seating_capacity = seating_capacity
class SchoolBus(School, Bus):
    def __init__(self, color , get_school_id, number_of_students, max_speed=0, mileage=0, seating_capacity=0):
        super().__init__(get_school_id, number_of_students)
        Bus.__init__(self, max_speed, mileage, seating_capacity)
        self.bus_school_color = color

sb = SchoolBus("red", 85, 500, 120, 400, 50)
print(sb.bus_school_color, sb.get_school_id, sb.number_of_students, sb.max_speed, sb.mileage, sb.seating_capacity)
# OUTPUT: red 85 500 120 400 50

# 7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method. Create two instances, one of Bear and one of Wolf, make a tuple of it and by using for call their action using the same method.
class Bear:
    def make_sound(self):
        print("RRRRRRRRR")
class Wolf:
    def make_sound(self):
        print("Woooooooo")

bear = Bear()
wolf = Wolf()
b_w = (bear, wolf)
for elem in b_w:
    elem.make_sound()
# OUTPUT: RRRRRRRRR
# OUTPUT: Woooooooo


# MAGIC METHODS:
# 8. Create class City with name, population instance attributes, return a new instance only when population > 1500,
# otherwise return message: "Your city is too small".
class City:
     def __new__(cls, name, population):
        if population > 1500:
            return super().__new__(cls)
        else:
            print("Your city is too small")
     def __init__(self, name, population):
         self.name = name
         self.population = population

w = City('City1', 1000)
print(w)
# OUTPUT: Your city is too small; None (no new object returned)
W = City('City2', 10000)
print(W)
# OUTPUT: <__main__.City object at 0x7f4dfb86a760>

# 9. Override a printable string representation of the City class and return: The population of the city {name} is {population}
class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population
    def __str__(self):
        return f"The population of the city {self.name} is {self.population}"

c = City('City3', 1000000)
print(c)
# OUTPUT: The population of the city City3 is 1000000

# 10*. Override magic method __add__() to perform the additional action as 'multiply' (*) the value which is greater than 10. And perform this add (+) of two instances.
class Dodavannya:
    def __init__(self, value):
        self.value = value
    def __add__(self, other):   # self = a1, other = a2
        if other.value > 10 or self.value > 10:    # other.value = a2.value (attribute of the second object a2); self.value = a1.value
            return other.value * self.value
        else:
            return other.value + self.value

a1 = Dodavannya(11)
a2 = Dodavannya(7)
print(a1 + a2)
# OUTPUT: 77
b1 = Dodavannya(5)
b2 = Dodavannya(3)
print(b1 + b2)
# OUTPUT: 8

# 11. The __call__ method enables Python programmers to write classes where the instances behave like functions and can be called like a function.
# Create a new class with __call__ method and define this call to return sum.
# (1)
class SumNumb:
    def __call__(self, *args):
        summa = 0
        summa = sum(args)
        return summa
s = SumNumb()
print(s(1, 2, 3, 4, 5, 5))
# OUTPUT: 20

# (2)
class SumNumb:
    def __call__(self, *args):
        summa = 0
        for i in args:
            summa += i
        return summa

s = SumNumb()
print(s(1, 2, 3))
print(s(1, 2, 3))
# OUTPUT: 6 6

# 12*. Making Your Objects Truthy or Falsey Using __bool__().
# Create class MyOrder with cart and customer instance attributes. Override the __bool__magic method considered to be truthy if the length of the cart list is non-zero.
class MyOrder:
    def __init__(self, cart=[], customer=''):
        self.cart = cart
        self.customer = customer

    def __bool__(self):
        if len(self.cart) != 0:
            return True
        else:
            return False

order_1 = MyOrder(['a', 'b', 'c'], 'd')
order_2 = MyOrder([], 'a')
print(bool(order_1))
# OUTPUT: True
print(bool(order_2))
# OUTPUT: False
