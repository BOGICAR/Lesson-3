# Задание №5 - сделано
import random
# Вариант №1
# Try №1
integer_number = int(input('''Try №1 
Please enter an integer number: '''))
random_number = random.randint(1, 10)
# print(random_number)
if integer_number == random_number:
    print('You won!')
else:
    print('You lose!')
# Try №2
integer_number = int(input('''Try №2 
Please enter an integer number: '''))
random_number = random.randint(1, 10)
# print(random_number)
if integer_number == random_number:
    print('You won!')
else:
    print('You lose!')
# Try №3
integer_number = int(input('''Try №3 
Please enter an integer number: '''))
random_number = random.randint(1, 10)
# print(random_number)
if integer_number == random_number:
    print('You won!')
else:
    print('You lose!')
# Вариант №2 - циклом
number_of_attempts = 0
while number_of_attempts < 3:
    integer_number = int(input('Please enter an integer number: '))
    random_number = random.randint(1, 10)
    if integer_number == random_number:
        print('You won!')
    else:
        print('You lose!')
    number_of_attempts += 1

