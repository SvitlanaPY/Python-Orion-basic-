# 1. Define the id of next variables:
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
print(id(int_a), id(str_b), id(set_c), id(lst_d), id(dict_e))
# OUTPUT: 9790336 139929085498032 139929085495104 139929086388544 139929086345984

# 2. Append 4 and 5 to the lst_d and define the id one more time.
lst_d.append(4)
lst_d.append(5)
print(id(lst_d))
# OUTPUT: 139929086388544 (it differs with every new program run)

# 3. Define the type of each object from step 1.
print(type(int_a), type(str_b), type(set_c), type(lst_d), type(dict_e))
# OUTPUT: <class 'int'> <class 'str'> <class 'set'> <class 'list'> <class 'dict'>

# 4*. Check the type of the objects by using isinstance.
def type_definition(v):
    if isinstance(v, str):
        print('type is str')
    elif isinstance(v, int):
        print('type is int')
    elif isinstance(v, list):
        print('type is list')
    elif isinstance(v, dict):
        print('type is dict')
    elif isinstance(v, set):
        print('type is set')
    elif isinstance(v, tuple):
        print('type is tuple')
    elif isinstance(v, float):
        print('type is float')

type_definition(int_a)    # OUTPUT: type is str
type_definition(str_b)    # OUTPUT: type is int
type_definition(set_c)    # OUTPUT: type is set
type_definition(lst_d)    # OUTPUT: type is list
type_definition(dict_e)   # OUTPUT: type is dict

# String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."

# 5. With .format and curly braces {}
print("Anna has {} apples and {} peaches.".format(int_a, int_a))
# OUTPUT: Anna has 55 apples and 55 peaches.

# 6. By passing index numbers into the curly braces.
print("Anna has {0} apples and {1} peaches.".format(10, 20))
# OUTPUT: Anna has 10 apples and 20 peaches.

# 7. By using keyword arguments into the curly braces.
print("Anna has {apples} apples and {peaches} peaches.".format(apples=15, peaches=25))
# OUTPUT: Anna has 15 apples and 25 peaches.

# 8*. With indicators of field size (5 chars for the first and 3 for the second)
print("Anna has {0:5} apples and {1:3} peaches.".format(1, 2))
# OUTPUT: Anna has     1 apples and   2 peaches.

# 9. With f-strings and variables
apple = 11
peach = "ten"
print(f"Anna has {apple} apples and {peach} peaches.")
# OUTPUT: Anna has 11 apples and ten peaches.

# 10. With % operator
green_apples = 'nine'
ripe_peaches = 55
print("Anna has %s apples and %d peaches." % (green_apples, ripe_peaches))
# OUTPUT: Anna has nine apples and 55 peaches.

# 11*. With variable substitutions by name (hint: by using dict)
app = 5
pch = "two"
fruits_dict = {'one': app, 'two': pch}
print("Anna has %(one)d apples and %(two)s peaches." % fruits_dict)
# OUTPUT: Anna has 5 apples and two peaches.

#
# COMPREHENSIONS:
# (1)
# lst = []
# for num in range(10):
#     if num % 2 == 1:
#         lst.append(num ** 2)
#     else:
#         lst.append(num ** 4)
# print(lst)
#
# (2)
# list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
#

# (3)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
# print(d)
#
# (4)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
#     else:
#         d[num] = num // 0.5
# print(d)
#
# (5)
# dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
#
# (6)
# dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}

# 12. Convert (1) to list comprehension
list_comprehension = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(list_comprehension)
# OUTPUT: [0, 1, 16, 9, 256, 25, 1296, 49, 4096, 81]

# 13. Convert (2) to regular for with if-else
list_comprehension = []
for num in range(10):
    if num % 2 == 0:
        list_comprehension.append(num // 2)
    else:
        list_comprehension.append(num * 10)
print(list_comprehension)
# OUTPUT: [0, 10, 1, 30, 2, 50, 3, 70, 4, 90]

# 14. Convert (3) to dict comprehension.
dict_comprehension1={num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(dict_comprehension1)
# OUTPUT: {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# 15*. Convert (4) to dict comprehension.
dict_comprehension2 = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(dict_comprehension2)
# OUTPUT: {1: 1, 2: 4.0, 3: 9, 4: 8.0, 5: 25, 6: 12.0, 7: 49, 8: 16.0, 9: 81, 10: 20.0}

# 16. Convert (5) to regular for with if.
dd = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dd[x] = x**3
print(dd)
# OUTPUT: {0: 0, 2: 8, 4: 64, 6: 216, 8: 512}

# 17*. Convert (6) to regular for with if-else.
ddd = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        ddd[x] = x**3
    else:
        ddd[x] = x
print(ddd)
# OUTPUT: {0: 0, 1: 1, 2: 8, 3: 3, 4: 64, 5: 5, 6: 216, 7: 7, 8: 512, 9: 9}

# LAMBDA:
# (7)
# def foo(x, y):
#     if x < y:
#         return x
#     else:
#         return y
#
# (8)
# foo = lambda x, y, z: z if y < x and x > z else y

# 18. Convert (7) to lambda function
foo = lambda x, y: x if x < y else y
print(foo(5, 3))
# OUTPUT: 3

# 19*. Convert (8) to regular function
def foo(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y
print(foo(5, 3, 1))
# OUTPUT: 1


lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
#
# 20. Sort lst_to_sort from min to max
print(sorted(lst_to_sort))
# OUTPUT: [1, 5, 13, 15, 18, 24, 33, 55]

# 21. Sort lst_to_sort from max to min
print(sorted(lst_to_sort, reverse = True))
# OUTPUT: [55, 33, 24, 18, 15, 13, 5, 1]

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2
print(list(map(lambda x: x * 2, lst_to_sort)))
# OUTPUT: [10, 36, 2, 48, 66, 30, 26, 110]

# 23*. Raise each list number to the corresponding number on another list:
list_A = [2, 3, 4]
list_B = [5, 6, 7]
print(list(map(lambda x, y: x ** y, list_A, list_B)))
# OUTPUT: [32, 729, 16384]

# 24. Use reduce and lambda to compute the numbers of a lst_to_sort.
from functools import reduce
def summ_elements(x1, x2):
    return x1 + x2
print(reduce(summ_elements, lst_to_sort))
# OUTPUT: 164

# 25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
print(list(filter(lambda elem: elem % 2 == 1, lst_to_sort)))
# OUTPUT: [5, 1, 33, 15, 13, 55]

# 26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
print(list(filter(lambda x: x < 0, range(-10, 10))))
# OUTPUT: [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

# 27*. Using the filter function, find the values that are common to the two lists:
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]
common = list(filter(lambda x: x in list_2, list_1))
print(common)
# OUTPUT: [2, 3, 5, 7]