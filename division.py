import time
import random
import os
import platform

def clear():
    if platform.system() == "Linux":
        os.system('clear')
    elif platform.system() == "Windows":
        os.system('cls')

numbers = list(range(1,100))
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
            clear()
    print('Your Division score is:', score, '/ 10')
