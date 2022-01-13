def a(x):
    s = 0
    while x > 0:
        x = x // 10
        s += 1
    return s


x = abs(int(input('Введите число:')))
print('Количество разрядов:', a(x))
