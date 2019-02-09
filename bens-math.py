import time
import random
import os
import platform
from division import *

#Clears output to make it easier to read
def clear():
    if platform.system() == "Linux":
        os.system('clear')
    elif platform.system() == "Windows":
        os.system('cls')
numbers = list(range(1,100))

#Main Menu
print('Program only tested in Python3. Stability in Python2 is not guaranteed')
input('\nPress ENTER key to acknowledge and continue...')
clear()
print("Welcome to Ben's Math program v5.0!")
input('\nPress ENTER key to and continue...')
clear()

def arithmetic(type, title, numQuestions):
    print(title)
    time.sleep(1)
    clear()
    score = 0
    for x in range(numQuestions):
        number1 = random.choice(numbers)
        number2 = random.choice(numbers)

        solution = 0;
        if type == "addition" :
            print('What is', number1, '+', number2, '?')
            solution = number1 + number2;
        elif type == "subtraction" :
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
            print('Invalid input detected...')
            exit(12)
        elif solution == int(answer):
            time.sleep(1)
            score += 1
        else:
            score += 0
        time.sleep(1.5)
        clear()

    print('Your score is:', score,'/',numQuestions)
    input('Press ENTER key to advance to next level...')
    clear()
    score = 0

#modifies the level names and number of Questions
arithmetic('addition', 'Level 1: Addition', 1)
arithmetic('subtraction', 'Level 2: Subtraction', 1)
arithmetic('multiplication', 'Level 3: Multiplication', 1)

division()
time.sleep(1)
clear()
