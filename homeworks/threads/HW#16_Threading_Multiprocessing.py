"""
1. Написати програму яка буде обраховувати два квадратних рівняня одночасно,
всі параметри рівняння задати в змінні.
"""

import logging
from math import sqrt
from random import randint
from time import time, sleep
import threading

FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(filename="Math_Equation.log", level=logging.INFO, filemode='a', format=FORMAT)

def equation(a, b, c, func_name):
    for i in range(20):
        sleep(randint(0, 1))
        logging.info("'Equation{}' assigned to thread: {}".format(func_name, threading.current_thread().name))
        print("'Equation{}' assigned to thread: {}".format(func_name, threading.current_thread().name))
        d = b ** 2 - 4 * a * c
        if d > 0:
            x1 = ((-b) + sqrt(d)) / (2 * a)
            x2 = ((-b) - sqrt(d)) / (2 * a)
            logging.info(f"D > 0: x1= {x1} and x2= {x2}")
            print(f"D > 0: x1= {x1} and x2= {x2}")
        elif d == 0:
            x1 = (-b) / (2 * a)
            logging.info(f"D == 0: x1= {x1}")
            print(f"D == 0: x1= {x1}")
        else:
            logging.info("D < 0: No solution for equation1")
            print("D < 0: No solution for equation1")


if __name__ == "__main__":
    logging.info("Main thread name: {}".format(threading.main_thread().name))
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

    logging.info("working time= {}".format(round((finish_time - start_time), 2)))
    print("\nworking time =", round((finish_time - start_time), 2))

    print("DONE!")
