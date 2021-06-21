# Задание №1 - сделано
# Вариант №1 - если число будет из 3 цифры (суммирует первые 3 цифры)
entered_number = input('Please enter an integer number: ')
first_digit = int(entered_number[0])
second_digit = int(entered_number[1])
third_digit = int(entered_number[2])
sum_of_digits = first_digit + second_digit + third_digit
print('Sum of digits: ', sum_of_digits)
# Вариант №2 - число может быть любым
sum_of_digits = 0
for symbol in entered_number:
    sum_of_digits += int(symbol)
print('Sum of digits: ', sum_of_digits)
