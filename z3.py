import math


def square():
    a = int(input('Введите сторону'))
    c = math.sqrt(a ** 2 + a ** 2)
    return ('Периметр', a + a + a + a), ('Площадь', a ** 2), c


print(square())
