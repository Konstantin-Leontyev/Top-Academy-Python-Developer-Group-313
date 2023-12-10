# w, h = 4, 3
# matrix = [[0 for x in range(w)] for y in range(h)]

# matrix = []
# for y in range(h):
#     new_row = []
#     for x in range(w):
#         new_row.append(0)
#     matrix.append(new_row)
# print(matrix)
#
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()

# from random import randint
# w, h = 4, 3
# matrix = [[randint(1, 30) for x in range(w)] for y in range(h)]
#
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()

from random import randint

w, h = 3, 4
matrix = [[randint(-20, 10) for x in range(w)] for y in range(h)]
#
# for row in matrix:
#     for x in row:
#         print(x, end='\t\t')
#     print()
#
# count = 0
# for row in matrix:
#     for x in row:
#         if x < 0:
#             count +=1
#
count = 0
for row in matrix:
    for x in row:
        if x < 0:
            count += 1
        print(x, end='\t\t')
    print()

print('Количество отрицательных элементов: ', count)

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, '+',  y, '=', x + y)

# import math
# num1 = math.sqrt(4)
# num2 = math.ceil(3.1)
# num3 = math.floor(3.8)
#
# print(num1)
# print(num2)
# print(num3)
#
# print(math.pi)

# import math as m  # аналог from math import *
# from math import sqrt, ceil
# from math import *
#
# num1 = sqrt(4)
# num2 = ceil(3.1)
#
# print(num1)
# print(num2)
#
# import time
# import locale
#
# locale.setlocale(locale.LC_ALL, 'ru')
#
# seconds = time.time()
# print('Количество секунд: ', seconds)
#
# local_time = time.ctime(170158989)
# print('Местное время: ', local_time)
#
# res = time.localtime()
# print(res)
# print(res.tm_mday, '.', res.tm_mon, '.', res.tm_year, sep='')
#
# print(time.strftime('Today is %B %d, %Y'))
#
# # print(time.strftime('%d/%m/%Y, %H:%M:%S', time.localtime(170158989)))
#
# print(time.strftime('Сегодня: %B %d, %Y'))
#
# start = time.time()
# time.sleep(5)
# finish = time.time()
# res = finish - start
# print(res)
