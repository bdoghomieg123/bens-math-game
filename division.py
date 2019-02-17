import time
import random as rando
import os
import platform
from common import *
numbers = list(range(1,100))


def math(type, title, numQuestions):
    print(title)
    time.sleep(1)
    clear()
    score = 0
    for x in range(numQuestions):
        number1 = rando.choice(numbers)
        number2 = rando.choice(numbers)
        solution = 0;
        if type == "division":
            if number1 < number2:
                switch = number2
                number1 = number2
                number2 = switch
            print('What is', number1, 'divided by', number2, '?')
            solution = round(number1 / number2,1)
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
        print('Your division score is:', score,'/',numQuestions)
        input("Press ENTER to advance to next level...")



#arithmetic('division','Level 4: Division', 1)
