"""
1. Написати програму яка буде обраховувати два квадратних рівняня одночасно,
всі параметри рівняння задати в змінні.
"""
from math import sqrt
import threading
from time import time, sleep

def equation(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        lst = []
        x1 = ((-b) + sqrt(d)) / (2 * a)
        lst.append(x1)
        x2 = ((-b) - sqrt(d)) / (2 * a)
        lst.append(x2)
        return lst
    elif d == 0:
        x1 = (-b) / (2 * a)
        return x1

result1 = equation(1, 10, 21)
print(f"D > 0: x1= {result1[0]} and x2 = {result1[1]}")

result2 = equation(5, 0, 0)
print(f"D == 0: x = {result2}")

result3 = equation(4, 0, 36)
print("D < 0: No solutions for equation")
