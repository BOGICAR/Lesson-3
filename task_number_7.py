# Задание №7 - сделано
entered_number = int(input('Please enter an integer number: '))
factorial_of_entered_number = 1
while entered_number > 0:
    factorial_of_entered_number = factorial_of_entered_number * entered_number
    entered_number -= 1
print('Factorial of entered number = ', factorial_of_entered_number)