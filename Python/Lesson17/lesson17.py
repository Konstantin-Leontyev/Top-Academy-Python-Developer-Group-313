# def changeCharToStr(s, c_old, c_new):
#     return ''.join([x if x != c_old else c_new for x in s])
#
#
# str1 = 'Я изучаю Nython. Мне нравиться Nython. Nython очень интересный язык программирования'
# str2 = changeCharToStr(str1, 'N', 'P')
#
# print('str1 =', str1)
# print('str2 =', str2)


# print('C:\folder\file.txt')
# print('C:\\folder\\file.txt\\')
# print(r'C:\folder\file.txt\\'[:-1])
# print(r'C:\folder\file.txt' + "\\")

# name = 'Дмитрий'
# age = 25
# print(f'Меня зовут {name}. Мне {age} лет.')
#
# m = 2.58976415
# print(f'Число: {round(m, 2)}')
# print(f'Число: {m:.3f}')

# x = 10
# y = 5
#
# print('x = ', x, ', y = ', y, sep='')
# print(f'{x = }, {y = }')
#
# print(f'{x} x {y} / 2 = {x * y / 2}')

# num = 74
# print(f'{{{{num}}}}')
#
# dir_name = 'my_doc'
# file_name = 'data.txt'
# print(fr'home\{dir_name}\{file_name}')
# print('home\\' + dir_name + '\\' + file_name)

# s = """
# Многостро'чный' "новый"
# текст
# """
# print(s)
#
# s1 = '''
# Многострочный
# текст
# '''
# print(s1)
#
# s2 = 'Тек\nст'
# print(s2)

# def square(n):
#     """Принимает число n, возвращает квадрат число n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
# print()
# print(sum.__doc__)
# print()
# print(min.__doc__)
# print()
# print(len.__doc__)

# from math import pi
#
#
# def cyliber(r, h):
#     """
#     Calculate the radius of a cylindrical.
#
#     # Calculate the radius of a cylindrical by height and radius
#     # Вычисляет площадь цилиндра на основании заданной высоты и радиуса цилиндра
#     :Note пример
#     :param r: положительное число, радиус цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: class: `float` **radius** of a cylindrical
#     """
#     return 2 * pi * r * (r + h)
#
# print(cyliber(2, 4))

# print(ord('a'))  # 97
# print(ord('й'))  # 1081
#
# while True:
#     n = input ('-> ')
#     if n != '-1':
#         print(ord(n))
#     else:
#         break

# s = 'Test string for me'
# arr = [ord(x) for x in s]
# print('ASCII коды:', arr)
# from statistics import mean
# arr = [int(mean(arr))] + arr
# print('Средне арифметическое:', arr)
# arr += [ord(x) for x in input('-> ')[:3] if ord(x) not in arr]
# # if arr[-1] in arr[:-1]:
# #     arr.count(arr[-1])
# print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

print(chr(97))
print(chr(1048))

print('apple' == 'Apple')  # 97 == 65
print('apple' > 'Apple')  # 97 > 65