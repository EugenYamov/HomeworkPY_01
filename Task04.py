# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

def points_distance (xa, ya, xb, yb):

    result =  round(((((xb - xa) ** 2) + ((yb - ya) ** 2)) ** 0.5), 3)
    print ('Расстояние между точками = ', result)

xa =  float(input('Введите координату Х точки А: '))
ya =  float(input('Введите координату Y точки А: '))
xb =  float(input('Введите координату Х точки B: '))
yb =  float(input('Введите координату Y точки B: '))

points_distance (xa, ya, xb, yb)