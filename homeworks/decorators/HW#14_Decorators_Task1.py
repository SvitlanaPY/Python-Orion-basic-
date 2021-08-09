print("\nTASK1:")
"""
1. Дану задачу робити через декоратор як функції!
Написати декоратор який зробить з будь-якої функції строго типізовану. Тобо це декоратор який приймає аргументи.
Аргументами будуть типи даних, порядок аргументів декоратору відповідає порядку аргументів функції
Приклад:
@decor(int, float, int, float)
def func(1, 1.2, 4)
Зверніть увагу що декоратор приймає на 1 аргумент більше ніж функція, останній аргумент це строга типізація того, що
функція повертає
можете написати власний ексепшин і кидати його тоді коли тип даних не відповідає тому, що очікується
"""

def decor_out(*args_d):
    def decor_in(func_):
        def inner(*args_f):
            if len(args_d) == len(args_f) + 1:
                for i in range(len(args_f)):
                    if type(args_f[i]) != args_d[i]:   # isinstance((args_f[i]), args_d[i])
                        raise Exception("WRONG TYPE for function's argument")
            else:
                raise Exception("Function should get 1 parameter less than decorator!!!")
        return inner
    return decor_in


@decor_out(int, float, int, float)
def func(*args_f):
    pass


print(func(1, 2.2, 4.0))
