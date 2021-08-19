"""
1. Написати програму яка буде обраховувати два квадратних рівняня одночасно,
всі параметри рівняння задати в змінні.
"""


from math import sqrt
from random import randint
from time import time, sleep
import threading


def equation(a, b, c, func_name):
    for i in range(20):
        sleep(randint(0, 1))
        print("'Equation{}' assigned to thread: {}".format(func_name, threading.current_thread().name))
        d = b ** 2 - 4 * a * c
        if d > 0:
            lst = []
            x1 = ((-b) + sqrt(d)) / (2 * a)
            lst.append(x1)
            x2 = ((-b) - sqrt(d)) / (2 * a)
            lst.append(x2)
            print(f"D > 0: x1= {lst[0]} and x2= {lst[1]}")
        elif d == 0:
            x1 = (-b) / (2 * a)
            print(f"D == 0: x1= {x1}")
        else:
            print("D < 0: No solution for equation1")


if __name__ == "__main__":
    print("Main thread name: {}".format(threading.current_thread().name))
    # print("Main thread name: {}".format(threading.main_thread().name))

    t1 = threading.Thread(target=equation, name='t1', args=(1, 10, 21, 1,))
    t2 = threading.Thread(target=equation, name='t2', args=(5, 0, 0, 2,))

    start_time = time()

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    finish_time = time()

    print("\nworking time =", round((finish_time - start_time), 2))
    print("DONE!")
