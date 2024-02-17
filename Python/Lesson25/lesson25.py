# # Модификаторы доступа
# # public - name
# # protected - _name
# # private - __name
#
# class Point:
#     __slots__ = ['__x', '__y'] # Закрываем создание алиментов из вне
#
#     def __init__(self, x, y):
#         self.__x: int | float
#         self.__y: int | float
#         if self.__check_value(x) and self.__check_value(y):
#             self.__x = x
#             self.__y = y
#         # self.set_coordinates(x, y) # так не получиться, еще нет x и y
#
#     @classmethod
#     def __check_value(cls, c):
#         if isinstance(c, (int, float)):
#             return True
#         return False
#
#     def get_coordinates(self):
#         return self.__x, self.__y
#
#     # def set_coordinates(self, x, y):
#     #     if isinstance(x, (int, float)) and isinstance(y, (int, float)):
#     #         self.__x = x
#     #         self.__y = y
#     #     else:
#     #         print('Координаты должны быть числами')
#
#     def set_coordinates(self, x, y):
#         if self.__check_value(x) and self.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print('Координаты должны быть числами')
#
#     def get_x(self):
#         return self.__x
#
#     def set_x(self, x):
#         if self.__check_value(x):
#             self.__x = x
#         else:
#             print('Координата', x, 'должна быть числом')
#
#     def get_y(self):
#         return self.__y
#
#     def set_y(self, y):
#         if self.__check_value(y):
#             self.__y = y
#         else:
#             print('Координата', y, 'должна быть числом')
#
#
# p1 = Point(5, 10)
# # print(p1.x, p1.y)
# # p1.x = 100 # Создание нового свойства, но не изменение атрибута.
# # p1.y = 'abc'
# # print(p1.x, p1.y)
# # print(p1.__dict__)
# # p1._Point__x = 100
# # p1._Point__y = 50
# # print(p1._Point__x, p1._Point__y)
#
# # p1.set_coordinates(100, 200)
# # print(p1.get_coordinates())
# # print(p1._Point__x, p1._Point__y)
#
# # p1.set_coordinates(10.5, 15.5)
# # print(p1.get_coordinates())
# # print(p1._Point__check_value(5))
#
# # p1.set_x('100')
# # print(p1.get_x(), p1.get_y())
# # p1.set_y(30.4)
# # print(p1.get_x(), p1.get_y())
# # p1._Point__x = 'abc'
# # print(p1._Point__x)
# # print(p1.__dict__)
#
# class Point:
#     # __slots__ = ['__x', '__y']
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __get_x(self):
#         return self.__x
#
#     def __get_y(self):
#         return self.__y
#
#     def __set_x(self, x):
#         self.__x = x
#
#     def __del_x(self):
#         del self.__x
#
#     def __set_y(self, y):
#         self.__y = y
#
#     def __del_y(self):
#         del self.__y
#
#     x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 100
# # print(Point.__dict__)
# print(p1.__dict__)
# del p1.x
# print(p1.__dict__)


# class Point:
#     # __slots__ = ['__x', '__y']
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __get_x(self):
#         return self.__x
#
#     def __set_x(self, x):
#         if not isinstance(x, (int, float)):
#             raise TypeError('Устанавливаемое значение должно быть числом')
#         self.__x = x
#
#     def __del_x(self):
#         del self.__x
#
#     @property # Должен идти первым.
#     def y(self):
#         return self.__y
#
#     @y.setter
#     def y(self, y):
#         self.__y = y
#
#     @y.deleter
#     def y(self):
#         del self.__y
#
#     x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 100
# print(p1.__dict__)
# del p1.x
# print(p1.__dict__)
# p1.y = 500
# print(p1.__dict__)
# del p1.y
# print(p1.__dict__)


# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if not isinstance(new_kg, (int, float)):
#             raise TypeError('Килограммы задаются только числами')
#         self.__kg = new_kg
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#     def print_data(self):
#         print(self.kg, 'кг => ', end='')
#         print(self.to_pounds(), 'фунтов')
#
#
# weight = KgToPounds(12)
# # print(weight.kg, 'кг => ', end='')
# # print(weight.to_pounds(), 'фунтов')
# weight.print_data()
# weight.kg = 41
# # print(weight.kg, 'кг => ', end='')
# # print(weight.to_pounds(), 'фунтов')
# weight.print_data()


# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#     # get_count = staticmethod(get_count())
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
#
# print(Point.get_count())
# print(p2.get_count())

# class Change:
#     @staticmethod
#     def increment(number):
#         return number + 1
#
#     @staticmethod
#     def decrement(number):
#         return number - 1
#
# print(Change.increment(10), Change.decrement(10))
#
# class Math_matic:
#
#     @staticmethod
#     def get_max(*data):
#         return max(*data)
#
#     @staticmethod
#     def get_min(*data):
#         return min(*data)
#
#     @staticmethod
#     def get_average(*data):
#         from statistics import mean
#         return mean(*data)
#
#     # @staticmethod
#     # def factorial(n):
#     #     if n == 1:
#     #         return 1
#     #     else:
#     #         return Math_matic.factorial(n - 1) * n
#
#     @staticmethod
#     def get_factorial(number):
#         fact = 1
#         for i in range(1, number + 1):
#             fact *= i
#         return fact
#
#     @staticmethod
#     def get_factorial(number):
#         from math import factorial
#         return factorial(number)
#
#
# data = [3, 5, 7, 9]
#
# print(Math_matic.get_max(data))
# print(Math_matic.get_min(data))
# print(Math_matic.get_average(data))
# print(f'Факториал числа (5)', Math_matic.get_factorial(5))

from math import sqrt


class Square:
    __count = 0

    @staticmethod
    def square_triangle1(a, b, c):
        Square.__count += 1
        p = (a + b + c) / 2
        return sqrt(p * (p - a) * (p - b) * (p - c))

    @staticmethod
    def square_triangle2(a, b):
        Square.__count += 1
        return 0.5 * a * b

    @staticmethod
    def square_area(a):
        Square.__count += 1
        return a * a

    @staticmethod
    def square_rectangle(a, b):
        Square.__count += 1
        return a * b

    @staticmethod
    def get_count():
        return Square.__count


print('Площадь треугольника по формуле Герона:', Square.square_triangle1(3, 4, 5))
print('Площадь треугольника через основание и высоту:', Square.square_triangle2(6, 7))
print('Площадь квадрата:', Square.square_area(7))
print('Площадь прямоугольника:', Square.square_rectangle(2, 6))
print('Количество подсчетов площади:', Square.get_count())

