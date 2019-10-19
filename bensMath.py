import time
import random as rando
import os
from division import math
from common import *


numbers = list(range(1,10))


#Main Menu
print('Program only tested in Python3. Stability in Python2 is not guaranteed')
input('\nPress ENTER key to acknowledge and continue...')
clear()
print("Welcome to Ben's Math program Beta v3.3.1!")
#hacker voice: "I'm in bois"
input('\nPress ENTER key to continue...')
clear()


def arithmetic(type, title, numQuestions):
    print(title)
    time.sleep(1)
    clear()
    score = 0
    for x in range(numQuestions):
        number1 = rando.choice(numbers)
        number2 = rando.choice(numbers)

        solution = 0;
        if type == "addition" :
            print('What is', number1, '+', number2, '?')
            solution = number1 + number2;
        elif type == "subtraction":
            if number1 < number2:
                switch = number2
                number1 = number2
                number2 = switch
            print('What is', number1, '-', number2, '?')
            solution = number1 - number2;
        elif type == "multiplication" :
            print('What is', number1, 'x', number2, '?')
            solution = number1 * number2;


        answer = input('\n')
        if answer == "":
            clear()
            print('Invalid input detected...')
            exit(123)
        elif solution == int(answer):
            clear()
            print("Correct Answer!\n")
            input("Press ENTER key to continue...\n")
            score += 1
            clear()
        elif solution != int(answer):
            clear()
            print("Sorry. That is incorrect.")
            input("Press ENTER key to continue")
            clear()
            score += 0
        time.sleep(1.5)
        clear()

    print('Your score is:', score,'/',numQuestions)
    input('Press ENTER key to advance to next level...')
    clear()
    score = 0


#modifies the level names and number of Questions
arithmetic('addition', 'Level 1: Addition', 2)
arithmetic('subtraction', 'Level 2: Subtraction', 0)
arithmetic('multiplication', 'Level 3: Multiplication', 0)
math('division','Level 4: Division', 1)
input("Press ENTER to advance to next level...")
clear()
