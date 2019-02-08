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

print('Program only tested in Python3. Running in Python2 is not recommended')
input('\nPress ENTER key to acknowledge and continue...')
clear()
print("Welcome to Ben's Math program. There are currently 2 levels. Addition and Multiplication. More to come soon!")
input('\nPress ENTER key to and continue...')
clear()
print("Level 1: Addition")
time.sleep(1)
clear()
numbers = [1,2,3,4,5,6,7,8,9,10]
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
    time.sleep(1)
    clear()
score = 0
print('Your addition score is:',score,'/ 10')
input('Press ENTER key to advance to level 2...')
print('Level 2: Multiplication')
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
    time.sleep(1)
    clear()
print('Your Multiplication score is:', score, '/10')
