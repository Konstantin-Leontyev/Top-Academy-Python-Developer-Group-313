from random import randint


def create_tuple(start: int, end: int) -> tuple:
    return tuple(randint(start, end) for _ in range(10))


tpl1 = create_tuple(0, 5)
tpl2 = create_tuple(-5, 0)
tpl3 = tpl1 + tpl2

print(tpl1, tpl2, tpl3, '0 = ' + str(tpl3.count(0)), sep='\n')
