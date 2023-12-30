from math import pi

methods_list = [
    lambda x: print(f'Площадь окружности радиуса {x}: {x ** 2 * pi}'),
    lambda x, y: print(f'Площадь прямоугольника размером {x}*{y}: {x * y}'),
    lambda a, b, h: print(f'Площадь трапеции a={a}, b={b}, h={h}: {(a + b) * h/2}'),
]

methods_list[0](2)
methods_list[1](10, 13)
methods_list[2](7, 5, 3)
