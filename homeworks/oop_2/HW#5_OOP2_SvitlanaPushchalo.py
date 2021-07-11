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


print('\n########## 5* ##########')
# class Concert:
#     """
#     Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
#     In case of setting visitors_count - max_visitors_num should be checked,
#     if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
#     Example:
#         Concert.max_visitor_num = 50
#         concert = Concert()
#         concert.visitors_count = 1000
#         print(concert.visitors_count)  # 50
#     """

class Concert:
    max_visitors_num = 0
    def __init__(self, visitors_count = 0):
        self.visitors_count = visitors_count

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, count):
        self._visitors_count = count if count <= Concert.max_visitors_num else Concert.max_visitors_num

Concert.max_visitors_num = 50
concert = Concert()
concert.visitors_count = 10
print(concert.visitors_count)
# OUTPUT: 50
Concert.max_visitors_num = 50
concert = Concert()
concert.visitors_count = 10
print(concert.visitors_count)
# OUTPUT: 10


print('\n########## 6 ##########')
# class AddressBookDataClass:
#     """
#     Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str), birthday (str), age (int)
#     """

from dataclasses import dataclass
@dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int

address_book = AddressBookDataClass(101,
                               'John Smith',
                               '(888) 558-9004',
                               '123 Main St, Pasadena, CA',
                               ' jsmith@comcast.net',
                               '01 January 2000',
                               21)
print(address_book)
# OUTPUT: AddressBookDataClass(key=10, name='John Smith', phone_number='(888) 558-9004', address='123 Main St, Pasadena, CA', email=' jsmith@comcast.net', birthday='01 January 2000', age=21)
print(address_book.name)
# OUTPUT: John Smith


print('\n########## 7 ##########')
# Create the same class (6) but using NamedTuple

from collections import namedtuple
AddressBookNamedTuple = namedtuple('AddressBookNamedTuple', ['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])
ab = AddressBookNamedTuple('10', 'John Smith', '(888) 558-9004', '123 Main St, Pasadena, CA', ' jsmith@comcast.net', '01 January 2000', '21')
print(ab)
# OUTPUT: AddressBookNamedTuple(key='10', name='John Smith', phone_number='(888) 558-9004', address='123 Main St, Pasadena, CA', email=' jsmith@comcast.net', birthday='01 January 2000', age='21')
print(ab[0:3])
# OUTPUT: ('10', 'John Smith', '(888) 558-9004')
print('address:', ab.address)
# OUTPUT: address: 123 Main St, Pasadena, CA


print('\n########## 8 ##########')
# class AddressBook:
#     """
#     Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
#     Make its str() representation the same as for AddressBookDataClass defined above.
#     """

class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
    def __str__(self):
        return f"AddressBook(key={self.key}, name='{self.name}', phone_number='{self.phone_number}', address='{self.address}', email='{self.email}', birthday='{self.birthday}', age='{self.age}')"

a_b = AddressBook(10, 'John Smith', '(888) 558-9004', '123 Main St, Pasadena, CA', ' jsmith@comcast.net', '01 January 2000', 21)
print(a_b)
# OUTPUT: AddressBook(key=10, name='John Smith', phone_number='(888) 558-9004', address='123 Main St, Pasadena, CA', email=' jsmith@comcast.net', birthday='01 January 2000', age='21')


print('\n########## 9 ##########')
# class Person:
#     """
#     Change the value of the age property of the person object
#     """
#     name = "John"
#     age = 36
#     country = "USA"

class Person:
    def __init__(self, name, country, age = 0):
        self.name = name
        self.country = country
        self.age = age

    @property
    def age(self):
        # print('Get age')
        return self._age

    @age.setter
    def age(self, new_age):
        # print('Set age')
        self._age = new_age

person = Person('John', 'USA', 36)
print(person.age)
# OUTPUT: 36
person.age = 25   # save value in property age (call setter)
print('new age=', person.age)
# OUTPUT: new age= 25


print('\n########## 10 ##########')
# class Student:
#     """
#     Add an 'email' attribute of the object student and set its value
#     Assign the new attribute to 'student_email' variable and print it by using getattr
#     """
#     id = 0
#     name = ""
#
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name

class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

student = Student(101, 'Jim')
setattr(student, 'email', 'email_1@gmail.com')
student_email = 'email_2@gmail.com'        # create 'student_email' variable
setattr(student, 'email', student_email)
print('student.email=', getattr(student, "email"))
# OUTPUT: student.email= email2@gmail.com


print('\n########## 11* ##########')
# class Celsius:
#     """
#     By using @property convert the celsius to fahrenheit
#     Hint: (temperature * 1.8) + 32)
#     """
#     def __init__(self, temperature=0):
#         self._temperature = temperature
#
#
# # create an object
# {obj} = ...
#
# print({obj}.temperature)

class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def celsius_to_farenheit(self):
        return (self._temperature * 1.8) + 32

temp = Celsius(35)
print('temp. in fahrenheit:', temp.celsius_to_farenheit)
# OUTPUT: temp. in fahrenheit: 95.0

