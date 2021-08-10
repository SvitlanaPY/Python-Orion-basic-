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


def check_types(*args_d):
    def decor_in(summa_):
        def inner(*args_f):
            if len(args_d) == len(args_f) + 1:
                for i in range(len(args_f)):
                    if type(args_f[i]) != args_d[i]:   # not isinstance((args_f[i]), args_d[i])
                        raise Exception("WRONG TYPE for function's argument!!!")
                result = summa_(*args_f)
                if isinstance(result, args_d[-1]):
                    return result
                else:
                    raise Exception("Function should return float")
            else:
                raise Exception("Function should get 1 parameter less than decorator!!!")
        return inner
    return decor_in


@check_types(int, float, int, float)
def summa(*args_f):
    result = sum(args_f)
    return result


print(summa(1, 2.2, 4), "- function returns float")
# print(summa(1.0, 2.2, 4))   # ==> Exception("WRONG TYPE for function's argument!!!")
# print(summa(1, 2.2, 4, 5))  # ==> Exception("Function should get 1 parameter less than decorator!!!")
# @check_types(int, float, int, int) with print(summa(1, 2.2, 3)) ==>  Exception("Function should return float")