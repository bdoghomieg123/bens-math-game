import time
import random
import os
import platform
from common import *
import numpy as np
import matplotlib.pyplot as plt

numbers = list(range(1,100))
def functions():
    print('Level 5: Functions Practice')
    print('\nIn this section, plug in the given number for X in each problem')
    time.sleep(1)
    clear()
    score = 0
    for x in range(1):
        number1 = random.choice(numbers)
        number2 = random.choice(numbers)
        print("What is F(x) + ",number1)
        answer = input("\n")
        exit(32)



def troll(formula, x_range):
    print("Level 5 Functions Practice")
    time.sleep(2)
    print("Haha just joking. I don't know Alegebra\n")
    print("enjoy this graph until i figure it out for myself")
    time.sleep(5)
    x = np.array(x_range)
    y = eval(formula)
    plt.plot(x, y)
    plt.show()