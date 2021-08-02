print('Task1')
# """
# 1. Написати функцію яка в циклі зчитує з консолі введені користувачем дані і записує їх в список.
# Написати декоратор який видасть час виконання роботи функції
# """
from time import perf_counter
def decorator1(f_):
    def inner():
        start_time = perf_counter()
        f_()
        finish_time = perf_counter()
        working_time = round((finish_time - start_time), 2)
        return working_time
    return inner

@decorator1
def f():
    m = input('Enter some data: ')
    list_t = []
    while m != '.':
        list_t.append(m)
        m = input()
    return list_t

# f = decorator1(f)
print(f'function works {f()} seconds')


print()
print('Task2')
# """
# 2. Написати функцію яка приймає два катети і повертає значення гіпотензузи. Написати декоратор на функцію,
# який виводить на екран текст з довжиною катетів і гіпотенузи.
# Важливо! Функція повинно повернути саме значення гіпотенузи як число, а декоратор повинен зробити вивід на екран
# наприклад такого тексту “При катетах 3, 4 – гіпотенуза дорівнює 5”.
# """
def decorator2(hyp_):
    def inner(katet1, katet2):
        hp = hyp_(katet1, katet2)
        print(f"При катетах {katet1} та {katet2}, гіпотенуза буде {hp}")
        return hp
    return inner

@decorator2
def hyp(katet1, katet2):
    return (katet1 ** 2 + katet2 ** 2) ** 0.5

print(hyp(3, 4))


print()
print('Task3')
# """
# 3. Написати функцію яка приймає список елементів і знаходить суму, до функції написати декоратор який перед тим як
# запустити функцію видаляє з списку всі не чисельні типи даних, але якщо є строка яку можна перевести в число,
# (наприклад “1”) то строка приводиться до чисельного типу даних
# """
# def summa(*args):
#     sum_m = 0
#     for i in args:
#         if isinstance(i, (int, float)):
#             sum_m += i
#         elif isinstance(i, str):
#             try:
#                 i = float(i)
#             except ValueError:
#                 continue
#             else:
#                 sum_m += i
#     return sum_m
#
#
# print('SUM =', summa(5, 10, '4', 1, 'hi', 10.5, 6, '4.5'))


print()
print('Task4')
# """
# 4. Написати функцію яка приймає на вхід ціле число n створює і повертає список цілих чисел від 0 до n.
# Написати до цієї функції декоратор який всі елементи отриманого списку переведе в строковий тип даних
# """
def decorator(ff_):
    def inner():
        a = int(input('Enter some number: '))
        list_t = ff_(a)
        new_list = [str(elem) for elem in list_t]
        return new_list
    return inner

def ff(k):
    return list(range(k))

ff = decorator(ff)
# print(ff)   # <function decorator.<locals>.inner at 0x7f8f44d66280>
print(ff())


# (2):
def decorator(ff_):
    def inner():
        a = int(input('Enter some number: '))
        list_t = ff_(a)
        new_list = [str(elem) for elem in list_t]
        return new_list
    return inner

@decorator
def ff(k):
    return list(range(k))

print(ff())