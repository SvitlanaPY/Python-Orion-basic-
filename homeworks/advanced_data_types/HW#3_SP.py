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
