# crow = int(input('Введите количество ворон: '))
# case = ''
#
# if crow not in range(0, 10):
#     print('Ошибка ввода данных')
#     exit(1)
# elif crow == 1:
#     case = 'a'
# elif crow in range(2, 5):
#     case = 'ы'
# elif crow in range(5, 10) or crow == 0:
#     case = ''
#
# print(f'На ветке {crow} ворон{case}')


# password = input('Введите пароль: ')
#
# match password:
#     case 'qwerty':
#         print('Администратор')
#     case 'user':
#         print('Пользователь')
#     case _:
#         print('Неверный пароль')

# day = 'вторник'
# time = 17
#
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 16:
#         print('Рабочий день')
#     case 'суббота' | 'воскресенье':
#         print('Выходной день')
#     case _:
#         print('Такого дня недели не существует или не рабочее время')

# a, b = 10, 20
#
# print(a if a < b else b)

# a, b = 10, 20
#
# print('a == b' if a < b else 'a > b' if a > b else 'b > a')

# a = int(input('Введите числитель: '))
# b = int(input('Введите знаменатель: '))
# print('Результат:', a / b) if b else print('На ноль делить нельзя')
# print('Результат:', a / b if b else print('На ноль делить нельзя')

# try:
#     n = int(input('Введите целое число: '))
#     print(n * 2)
# except ValueError:
#     print('Что-то пошло не так')
#
# print('Следующая строка')

# try:
#     n = int(input('Введите делимое: '))
#     m = int(input('Введите делитель: '))
#     print(n / m)
# except ValueError:
#     print('Нельзя вводить строки')
# except ZeroDivisionError:
#     print('На ноль делить нельзя')

# try:
#     n = int(input('Введите делимое: '))
#     m = int(input('Введите делитель: '))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print('Нельзя вводить строки или на ноль делить нельзя')
# else:  # отрабатывает когда в блоке try не возникло исключения
#     print('Все нормально. Вы введи числа', n, "и", m)
# finally:  # отработает в любом случае
#     print('Конец программы')

# n = input('Введите делимое: ')
# m = input('Введите делитель: ')
#
# try:
#     n = int(n)  # n = число
#     m = int(m)  # m = строка
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)


# Циклы
# while

# i = 0
# while i < 5:
#     print('i = ', i)
#     i += 1

# i = 10
# while i > 0:
#     print('i = ', i)
#     i -= 1

# i = 0
# while i <= 20:
#     if not i % 2:
#         print('i = ', i)
#     i += 1

# count = int(input('Введите кол-во символов: '))
# i = 0
# while i <= count:
#     print('*', end='')
#     i += 1
#
# print('*' * count)

a = int(input('Введите кол-во символов: '))
b = int(input('Введите кол-во символов: '))
# res = None
# i = 0
#
# # for c = i % 2 in range(a, b + 1):
# #     res += i
# #     i += 1


if not a % 2:
    print(a % 2)
    i = a - 1

res = a
for i in range(a, b + 1):
    res += i
    i += 2
    print(res)
print(res)
