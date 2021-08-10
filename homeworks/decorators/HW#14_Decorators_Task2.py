print("\nTASK2:")
"""
2. Те ж саме що й в завданні 1, але зробити через функтор
"""


class WrongType(Exception):
    pass


class CheckTypes:
    def __init__(self, *args_d):
        self.args_d = args_d

    def __call__(self, summa_):
        def inner(*args_f):
            if len(self.args_d) == len(args_f) + 1:
                for i in range(len(args_f)):
                    if type(args_f[i]) != self.args_d[i]:   # not isinstance((args_f[i]), self.args_d[i])
                        raise WrongType
                result = summa_(*args_f)
                if isinstance(result, self.args_d[-1]):
                    return result
                else:
                    raise Exception("Function should return float")
            else:
                raise Exception("Function should get 1 parameter less than decorator!!!")
        return inner


@CheckTypes(int, float, int, float)
def summa(*args_f):
    result = sum(args_f)
    return result


print(summa(1, 2.2, 4), "- function returns float")
# print(summa(1.0, 2.2, 4))   # ==> Exception("WRONG TYPE for function's argument!!!")
# print(summa(1, 2.2, 4, 5))  # ==> Exception("Function should get 1 parameter less than decorator!!!")
# @check_types(int, float, int, int) with print(summa(1, 2.2, 3)) ==>  Exception("Function should return float")
