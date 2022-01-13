world = input('Введите слово:')
gl = 0
cgl = 0
vowels = 'аоэеиыуёюя'
c = ' ьъ!?,. '
for i in world:
    if i in vowels:
        gl += 1
    elif i in c:
        continue
    else:
        cgl += 1


def letters():
    return gl, cgl


print(letters())
