# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def coordinate_range (quater):

    if quater == 1:
        print ('X(0 : +∞); Y(0 : +∞)')
    
    if quater == 2:
        print ('X(-∞ : 0); Y(0 : +∞)')

    if quater == 3:
        print ('X(-∞ : 0); Y(-∞ : 0)')

    if quater == 4:
        print ('X(0 : +∞); Y(-∞ : 0)')

quater = int(input('Введите номер четверти от 1 до 4: '))

while quater < 1 or quater > 4:
    quater = int(input('Повторите ввод: '))

coordinate_range (quater)