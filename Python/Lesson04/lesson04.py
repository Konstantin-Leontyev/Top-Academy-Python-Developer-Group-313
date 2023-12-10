# n = input("Введите число: ")
#
# while type(n) is not int and type(n) is not float:
#     try:
#         n = int(n)
#     except ValueError:
#         try:
#             n = float(n)
#         except ValueError:
#             print('Число не целое и не вещественное!')
#             n = input("Введите число: ")
#
# if n * 10 % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')


# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue # пропускает текущую итерацию
#     print(i, end=" ")
#     if i == 5:
#         break # прерывает цикл
#     i += 1
# print("\nЦикл завершен")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input('Введите положительное число: '))
#     if n < 0:
#         break

# res = 1
# while True:
#     n = int(input('Введите число: '))
#     if n == 0:
#         break
#     res *= n
# print(res)

# i = 0
# while i < 10:
#     print(i, end=" ")
#     i += 1
# else:
#     print('\nЦикл окончен, i =', i)

# i = 1
# while i < 5:
#     print('Внешний цикл: i =', i)
#     j = 1
#     while j < 4:
#         print('\tВнутренний цикл: j =', j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         # print(f'{i} * {j} = {i * j}', end='\t\t')
#         print(i, '*', j, '=', i * j, end='\t\t')
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(' ', end='')
#         j += 1
#     print('*')
#     i += 1

# for element in collections:
#     print(element)

# for i in 'Hello', 'World', '!':
#     print(i)

# print(list(range(5)))

# range(start, stop, step) start=0 step=1

# for i in range(2, 9, 2):
#     print(i, end=' ')
#
# print()
# i = 2
# while i < 9:
#     print(i, end=' ')
#     i += 2
#
# for i in range(9, 0, -1):
#     print(i, end=' ')
#
# print()
# i = 9
# while i > 0:
#     print(i, end=' ')
#     i -= 2

# num = int(input('Введите целое число: '))
# for i in range(1, num + 1):
#     if not num % i:
#         print(i, end=' ')

start = int(input('Введите начало диапазона: '))
stop = int(input('Введите конец диапазона: '))
step = 11
if start < step:
    start = step
else:
    for i in range(start, stop):
        if i % 10 == i:
            start = i
            break

for i in range(start, stop + 1, step):
    print(i, end=' ')
