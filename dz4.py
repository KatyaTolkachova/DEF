a = int(input('Введите число секунд:'))
date = a // 86400
clock = (a - (date * 86400)) // 3600
minute = (a - ((date * 86400) + clock * 3600)) // 60
sec = a - ((date * 86400) + clock * 3600 + minute * 60)


def second():
    print(date, clock, minute, sec, sep=':')


second()
