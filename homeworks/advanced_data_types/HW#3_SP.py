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

