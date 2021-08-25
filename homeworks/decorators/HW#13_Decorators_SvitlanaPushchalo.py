from time import perf_counter
print("Task1")
# """
# 1. Написати функцію яка в циклі зчитує з консолі введені користувачем дані і записує їх в список.
# Написати декоратор який видасть час виконання роботи функції
# """
def decorator1(func_):
    def inner():
        start_time = perf_counter()
        func_()
        finish_time = perf_counter()
        return round((finish_time - start_time), 2)
    return inner

@decorator1
def func():
    m = input("Enter some data (or Q to exit): ")
    list_t = []
    while m != 'Q':
        list_t.append(m)
        m = input()
    return list_t

print(f'function works {func()} seconds')


print("\nTask2")
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

print("\nTask3")
# """
# 3. Написати функцію яка приймає список елементів і знаходить суму, до функції написати декоратор який перед тим як
# запустити функцію видаляє з списку всі не чисельні типи даних, але якщо є строка яку можна перевести в число,
# (наприклад “1”) то строка приводиться до чисельного типу даних
# """
def decorator3(summa_):
    def inner(list_t):
        new_list = []
        for i in list_t:
            try:
                i = float(i)
                new_list.append(i)
            except ValueError:
                continue
        return summa_(new_list)
    return inner

@decorator3
def summa(list_t):
    return sum(list_t)

lst = [5, 10, '4', 1, 'hi', 10.5, 6, '4.5', 5]
print(summa(lst))


print("\nTask4")
# """
# 4. Написати функцію яка приймає на вхід ціле число n створює і повертає список цілих чисел від 0 до n.
# Написати до цієї функції декоратор який всі елементи отриманого списку переведе в строковий тип даних
# """
def decor4(ff_):
    def inner():
        a = int(input('Enter some number: '))
        list_t = ff_(a)
        new_list = [str(elem) for elem in list_t]
        return new_list
    return inner

@decor4
def ff(k):
    return list(range(k+1))

print(ff())
