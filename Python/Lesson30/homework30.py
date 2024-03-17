class Point3D:
    # Задаем аннотацию для подсказок среды разработки
    def __init__(self, x: int | float, y: int | float, z: int | float):
        # Создаем словарь, что бы при проверке isinstance
        # получить доступ к имени переменной.
        # Для более развернутого писания ошибки.
        self.variables = {
            'x': x,
            'y': y,
            'z': z,
        }
        # Перебираем и проверяем в цикле
        for key, value in self.variables.items():
            if not isinstance(value, (int, float)):
                raise TypeError('Ошибка создания объекта класса Point3D. '
                                f'Проверьте значение координаты {key}. '
                                'Координаты задаются числавами значениями.')
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        """Метод строкового представления."""
        # Если хотя бы одна из координат
        # имеет дробное значение.
        if (isinstance(self.x, float)
            or isinstance(self.y, float)
            or isinstance(self.z, float)
        ):
            return f'({self.x:.1f}, {self.y:.1f}, {self.z:.1f})'
        # Если все координаты целые числа
        return f'({self.x}, {self.y}, {self.z})'

    def __add__(self, other):
        """Сложение двух классов Point3D."""
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Point3D(x, y, z)

    def __sub__(self, other):
        """Вычитание двух классов Point3D."""
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Point3D(x, y, z)

    def __mul__(self, other):
        """Умножение двух классов Point3D."""
        x = self.x * other.x
        y = self.y * other.y
        z = self.z * other.z
        return Point3D(x, y, z)

    def __truediv__(self, other):
        """Деление двух классов Point3D."""
        x = self.x / other.x
        y = self.y / other.y
        z = self.z / other.z
        return Point3D(x, y, z)

    def __eq__(self, other):
        """Сравнение двух классов Point3D."""
        if id(self) == id(other):
            return True
        if (
                self.x == other.x
                and self.y == other.y
                and self.z == other.z
        ):
            return True
        return False

    def __getitem__(self, item):
        """Получение значения координаты по ключу."""
        return self.variables[item]

    def __setitem__(self, key, value):
        """Запись значения координаты по ключу."""
        if not isinstance(key, str):
            raise TypeError('Ключ задаётся строковым значением')
        if not isinstance(value, int):
            raise TypeError('Координата задаётся числовым значением.')
        self.variables[key] = value


p1 = Point3D(12, 15, 18)
p2 = Point3D(6, 3, 9)

for index, value in enumerate([p1, p2], 1):
    print(f'Координаты {index}-ой точки {value}')

print(f'Сложение координат: {p1 + p2}')
print(f'Вычитание координат: {p1 - p2}')
print(f'Умножение координат: {p1 * p2}')
print(f'Деление координат: {p1 / p2}')
# Демонстрация, что работает и точечная нотация
# и доступ по ключу.
print(f'Равенство координат: {p1 == p2}\n'
      f'x = {p1.x} x1 = {p2["x"]}\n'
      f'y = {p1.y} y1 = {p2["y"]}\n'
      f'z = {p1.z} z1 = {p2["z"]}')
# # Если сравниваемые точки это один и тот же объект.
# p4 = p1
# print(id(p1))
# print(id(p4))
# print(f'Равенство координат: {p1 == p4}')
# Если точки имеют одинаковые координаты.
# p5 = Point3D(12, 15, 18)
# print(id(p1))
# print(id(p5))
# print(f'Равенство координат: {p1 == p5}')
p1['x'] = 20
print(f'Запись значения в координату x: {p1["x"]}')
