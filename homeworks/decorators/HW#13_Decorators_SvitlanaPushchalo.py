print('Task1')
# """
# 1. Написати функцію яка в циклі зчитує з консолі введені користувачем дані і записує їх в список.
# Написати декоратор який видасть час виконання роботи функції
# """
# def f():
#     m = input('Enter some data: ')
#     list_t = []
#     while m != '.':
#         list_t.append(m)
#         m = input()
#     return list_t
#
#
# print('list_t:', f())


print()
print('Task2')
# """
# 2. Написати функцію яка приймає два катети і повертає значення гіпотензузи. Написати декоратор на функцію,
# який виводить на екран текст з довжиною катетів і гіпотенузи.
# Важливо! Функція повинно повернути саме значення гіпотенузи як число, а декоратор повинен зробити вивід на екран
# наприклад такого тексту “При катетах 3, 4 – гіпотенуза дорівнює 5”.
# """
# def hyp(katet1, katet2):
#     hyp_p = (katet1 ** 2 + katet2 ** 2) ** 0.5
#     return hyp_p
#
# hp = hyp(3, 4)
# print('Hypotenuse =', hp)


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
def ff(k):
    return list(range(k))

def decorator(ff_):
    def inner():
        a = int(input('Enter some number: '))
        list_t = ff_(a)
        new_list = [str(elem) for elem in list_t]
        return new_list
    return inner

ff = decorator(ff)
# print(ff)   # <function decorator.<locals>.inner at 0x7f8f44d66280>
print(ff())

