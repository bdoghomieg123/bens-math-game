"""This File is not in use at the moment. It is the sad seed of level 5 at the moment."""

import time
import random
import os
import platform
import random as rando
from common import *
from sympy.solvers import solve
from sympy import Symbol
#solve(x**2 - 1, x)

x = Symbol('x')

#this is broken. Don't try to use it unless you wanna fix it. It should match the format of the other sections

def algebra(type, title, numQuestions):
    numbers = list(range(1,100))
    print('Level 5.1: Solving for X\n')
    print("For any non-whole numbers, round to the nearest hundredth")
    for x in range(numQuestions):
        number1 = rando.choice(numbers)
        number2 = rando.choice(numbers)
        number3 = rando.choice(numbers)
        solution = 0;
        if type == "solveforX":
            print("Solve for X in the following:\n")
            print()
            solution = round(solve(),2)
        answer = input('\n')
        if answer == "":
            print('Invalid input detected...')
            exit(420)
        elif solution == float(answer):
            time.sleep(1)
            score += 1
        else:
            score += 0
        time.sleep(1.5)
        clear()
    clear()
    print('Your division score is:', score,'/',numQuestions)
