# Задание №6 - сделано
x1 = int(input('Please enter x1: '))
y1 = int(input('Please enter y1: '))
x2 = int(input('Please enter x2: '))
y2 = int(input('Please enter y2: '))
delta_x = abs(x1 - x2)
delta_y = abs(y1 - y2)
if delta_x == 1 and delta_y == 2 or delta_x == 2 and delta_y == 1:
    print('The horse can go to this field')
else:
    print('The horse cannot go to this field')