# Задание №2 - сделано
entered_number = float(input('Please enter an integer number: '))
fractional_part_of_integer_number = entered_number * 100 % 100
fractional_part_of_integer_number = int(fractional_part_of_integer_number)
print('Fractional part of  integer number: ', fractional_part_of_integer_number)
fractional_part_of_integer_number = fractional_part_of_integer_number//10
print('First digit: ', fractional_part_of_integer_number)
