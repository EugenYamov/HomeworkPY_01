#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

def week (day):

    if day > 0 and day < 6:
        print ('Отстой, но это будний день')
    
    elif day > 5 and day < 8:
        print ('Yeah! Это выходной')

day = int(input('Введите число от 1 до 7: '))

if day > 0 and day < 8:
    week (day)
else:
    print('Число введено неверно, попробуйте снова')