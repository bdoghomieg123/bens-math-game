import time
import random as rando
import os
from common import *


def math(type, title, numQuestions):
    numbers = list(range(1,10))
    print(title)
    print("For this section, Please round to the nearest HUNDREDTH\n")
    input("Please press the ENTER key to continue...")
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
            solution = round(number1 / number2,2)
        answer = input('\n')
        if answer == "":
            print('Invalid input detected...')
            exit(420)
        elif solution == float(answer):
            print("Correct!\n")
            time.sleep(1)
            score += 1
        elif solution != float(answer):
            print("Sorry. That is incorrect\n")
            input("Press ENTER key to continue.\n")
            clear()
            score += 0
        time.sleep(1.5)
        clear()
    clear()
    print('Your division score is:', score,'/',numQuestions)
