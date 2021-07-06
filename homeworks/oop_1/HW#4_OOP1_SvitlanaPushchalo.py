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

# 7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method. Create two instances, one of Bear and one of Wolf,
# make a tuple of it and by using for call their action using the same method.
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
