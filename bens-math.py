import time
import random
import os
import platform

#Clears output to make it easier to read
def clear():
    if platform.system() == "Linux":
        os.system('clear')
    elif platform.system() == "Windows":
        os.system('cls')
numbers = list(range(1,100))

"""Main Menu"""
input('\nPress ENTER key to acknowledge and continue...')
print('Program only tested in Python3. Stability in Python2 is not guaranteed')
clear()
print("Welcome to Ben's Math program v2.0!")
input('\nPress ENTER key to and continue...')
clear()

#Addition Level
print("Level 1: Addition")
time.sleep(1)
clear()
score = 0
for x in range(10):
    number1 = random.choice(numbers)
    number2 = random.choice(numbers)
    question = number1 + number2
    print('What is', number1, '+', number2, '?')
    answer = input('\n')
    if answer == "":
        print('Invalid input detected...')
        exit(12)
    elif question == int(answer):
        time.sleep(1)
        score += 1
    else:
        score += 0
    time.sleep(1.5)
    clear()
print('Your addition score is:',score,'/ 10')
input('Press ENTER key to advance to level 2...')
clear()
score = 0

#Subtration level
print("Level 2: Subtraction")
time.sleep(1)
clear()
def subtraction():
    score = 0
    for x in range(10):
        number1 = random.choice(numbers)
        number2 = random.choice(numbers)
        question = number1 - number2
        print('What is', number1, '-', number2, '?')
        answer = input('\n')
        if answer == "":
            print('Invalid input detected...')
            exit(12)
        elif question == int(answer):
            time.sleep(1)
            score += 1

        else:
            score += 0
        time.sleep(1)
        clear()

    print('Your subtraction score is:',score,'/ 10')
    input('Press ENTER key to advance to level 3...')
subtraction()
clear()


#Multiplication Level
print('Level 3: Multiplication')
time.sleep(2)
clear()
for x in range(10):
    number1 = random.choice(numbers)
    number2 = random.choice(numbers)
    question = number1 * number2
    print('What is', number1, 'x', number2, '?')
    answer = input('\n')
    if answer == "":
        print('Invalid input detected...')
        exit(12)

    elif question == int(answer):
        time.sleep(1)
        score += 1
    else:
        score += 0
    time.sleep(2)
    clear()
print('Your Multiplication score is:', score, '/ 10')
input('\nPress ENTER key to continue to level 4...')
clear()
score = 0
def division():
    print('Level 4: Division')
    print('\nIn this section, round your answer to the first decimal place')
    time.sleep(3)
    clear()
    score = 0
    for x in range(10):
        number1 = random.choice(numbers)
        number2 = random.choice(numbers)
        if number1 < number2:
            division()
        else:
            question = round(number1 / number2, 1)
            print('What is', number1, 'divided by', number2, '?')
            answer = input('\n')
            if answer == "":
                print('Invalid input detected...')
                exit(12)
            elif question == float(answer):
                time.sleep(1)
                score += 1
            else:
                score += 0
            print('Your Division score is:', score, '/ 10')


division()
