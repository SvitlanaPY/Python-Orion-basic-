# """
# 1. Написати функцію яка в циклі зчитує з консолі введені користувачем дані і записує їх в список.
# Написати декоратор який видасть час виконання роботи функції
# """
def f():
    n = input()
    listt = []
    while n != '.':
        listt.append(n)
        n = input()
    return listt

print(f())


# """
# 2. Написати функцію яка приймає два катети і повертає значення гіпотензузи. Написати декоратор на функцію,
# який виводить на екран текст з довжиною катетів і гіпотенузи.
# Важливо! Функція повинно повернути саме значення гіпотенузи як число, а декоратор повинен зробити вивід на екран
# наприклад такого тексту “При катетах 3, 4 – гіпотенуза дорівнює 5”.
# """
def hyp(a, b):
    hyp = (a ** 2 + b ** 2) ** 0.5
    return hyp

print(hyp(3,4))


# """
# 3. Написати функцію яка приймає список елементів і знаходить суму, до функції написати декоратор який перед тим як
# запустити функцію видаляє з списку всі не чисельні типи даних, але якщо є строка яку можна перевести в число,
# (наприклад “1”) то строка приводиться до чисельного типу даних
# """
def summa(*args):
    summ = 0
    for i in args:
        if isinstance(i, (int, float)):
            summ = summ + i
        elif isinstance(i, str):
            try:
                i = float(i)
            except ValueError:
                continue
            else:
                summ = summ + i
    return summ

print(summa(5, 10, '4', 1, 'hi', 10.5, 6, '4.5'))


# """
# 4. Написати функцію яка приймає на вхід ціле число n створює і повертає список цілих чисел від 0 до n.
# Написати до цієї функції декоратор який всі елементи отриманого списку переведе в строковий тип даних
# """
n = int(input('Enter some number: '))
def ff(n):
    return list(range(n))

print(ff(n))