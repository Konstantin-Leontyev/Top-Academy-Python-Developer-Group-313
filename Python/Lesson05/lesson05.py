# for i in range(3):  # 0 1 2
#     print('+++ i =', i)
#     for j in range(2):  # 0 1
#         print('----- j =', j)

# h = input('Введите высоту прямоугольника: ')
# w = input('Введите ширину прямоугольника: ')
# w = 16
# h = 4
#
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# nums = [letter * 2 for letter in 'Banana']
# nums = [i for i in range(30) if i % 2 == 0]
# print(nums)

# Список (list)
# nums = []
# nums = [8, 3, 9, 4, 1, 'one']
# print(nums)
# # print(type(nums))
# #
# # print(nums[0])
# # print(nums[2])
# # # print(nums[6])  # IndexError
# #
# # print(nums[-1])
# # print(nums[-2])
# #
# # nums[1] = 256
# # print(nums)
# #
# # nums[3] += 100
# # print(nums)
# print(len(nums))

# for i in range(len(nums)):
#     print(nums[i] ** 2)

# s = []
# print(s)
#
# a = 5
# print(int('3') + a)
#
# b = list()
# print(b)
#
# b = list('Hello')
# print(b)

# print(range(0, 6))
# n = list(range(0, 6))
# print(n)
#
# print(list(range(10)))

# Генератор списка
# [выражение for переменная in последовательность]

# a = [0 for i in range(5)]
# print(a)
#
# a = [0 for _ in range(5)]
# print(a)

# b = [i for i in range(5)]
# print(b)

# n = 5
# b = [i ** 2 for i in range(1, n + 1)]
# print(b)

# a, b = [1, 2, 3], [4, 5]
# c = a + b
# print(c)
# d = b * 3
# print(d)

# a = [0] * int(input('Введите количество элементов списка: '))
# print(a)
#
# for i in range(len(a)):
#     # a[i] = input('-> ')
#     a[i] = int(input('-> '))
#
# print(a)

# a = [for i in range(int(input('Введите количество элементов списка: ')))]
# print(a)

# value = 0
# a = [int(input('-> ')) for i in range(int(input('Введите количество элементов списка: ')))]
# for element in a:
#     if element < 0:
#         value += element
#
# print(a)
#

# n = int(input('Введите количество элементов списка: '))
# a = [int(input('-> ')) for _ in range(n)]
#
# sum_negative = sum([num for num in a if num < 0])
# print('Сумма отрицательных элементов:', sum_negative)

# n = list(range(21, 41, 2))
# print(n)
# a = 2
# print(n[a])
# print(n[a - 1])
# print(n[a + 1])

# a = [int(input('-> ')) for _ in range(int(input('n = ')))]
# print(a)
# for i in range(1, len(a)):
#     # print(a[i], '-> ', end='')
#     # print(a[i - 1])
#     if a[i] > a[i - 1]:
#         print(a[i], end=' ')

