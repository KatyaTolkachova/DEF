a = float(input('Введите число'))
b = float(input('Введите число'))


def sm(a, b):
    return a + b


def pro(a, b):
    return a * b


def rth(a, b):
    return a - b


def de(a, b):
    if b != 0:
        return a / b
    else:
        return 'ДЕЛЕНИЕ НА НОЛЬ!!!'


while True:
    c = input('Введите операцию:')

    if c == '0':
        break
    else:
        if c == '+':
            print('Ответ:', sm(a, b))
        if c == '*':
            print('Ответ:', pro(a, b))
        if c == '-':
            print('Ответ:', rth(a, b))
        if c == '/' and b != 0:
            print('Ответ:', de(a, b))
