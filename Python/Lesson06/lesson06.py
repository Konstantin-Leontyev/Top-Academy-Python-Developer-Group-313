# a = [7, 8, 2, 1, 17, 9]
# print(a)
# a[0], a[1] = a[1], a[0]
# print(a)

# print(a[1:4])
# print(a[1:])
# print(a[:3])
# print(a[5:2:-1])
# print(a[10:20])
# b = a[10:20]
# print(b)

# a = list(range(1, 8))
# print(a)
# print(a[::-1])
# print(a[::2])
# print(a[1::2])
# print(a[:1])
# print(a[:-1])
# print(a[3:4])
# print(a[-3:])
# print(a[-3:1:-1])
# print(a[2:5])

# s = [5, 9, 3, 7, 1, 8]
# print(s)
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]  # присвоение через срез
# print(s)
# s[4:] = []
# print(s)
# # s[2:5] = []
# # del s[1]
# # del s[2:5]
# del s[:]
# print(s)

# s = [5, 9, 3, 7, 1, 8]
# print(s)
# s.append(99)  # добавляет элемент в конец списка
# # s.append([99, 1])  # принимает только один элемента
#
# print(s)
# s.extend([1, 2, 3])  # добавляет список элементов в конец списка
# # s.extend(1, 2, 3) # работает только с итерируемыми объектами s.insert('add')
# print(s)
# s.insert(0, 100)  # добавляет элемент (второй параметр), в заданный индекс (первый параметр)
# print(s)
# s.insert(20, 200)  # если указать за пределами списка добавит в конец
# print(s)
# s.insert(len(s), 200)
# print(s)

# s = []
# n = int(input('Кол-во элементов в списке: '))
# for num in range(n):
#     x = int(input('Введите число:'))
#     # s.append(x)
#     s.insert(0, x)
# print(s)

# s = []
# n = int(input('Кол-во элементов в списке: '))
# for num in range(n):
#     x = int(input('Введите число кратное 3: '))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, 'не делится на три без остатка')
#
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c: # если i находится в с
#             continue
#         if i == j:
#             c.append(i)
#             break

# for i in a:
#     if i not in c:
#         for j in b:
#             if i == j:
#                 c.append(i)
#                 break

# for i in a:
#     if i not in c and i in b:
#         c.append(i)
#
# print(c)  # [2, 1, 4 ,3]

# a = [1, 2, 3, 44, 55]
# b = [11, 22, 33]
# c = []
#
# # for i, j in zip(a, b):
# #     c.append(i)
# #     c.append(j)
#
# if len(a) > len(b):
#     a, b = b, a
#
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(a[i])
#
# print(c)

# s = [5, 9, 3, 7, 9, 1, 8, 9]
# print(s)
# print(s.remove(9))  # удаляет первый найденный элемент по заданному значению
# print(s)
# s.pop()  # без параметров - удаляет последний элемент из списка
# print(s)
# a = s.pop(-1)
# print(a)
# print(s)
# s.clear()  # очистка всех элементов списка
# print(s)

# # numbers = [int(input('-> ')) for _ in range(int(input('n = ')))]
# numbers = [6, 4, 7, 8, 9]
# index = int(input('Введите индекс удаляемого элемента: '))
# numbers.pop(index)
# print(numbers)

# s = [5, 9, 3, 7, 9, 1, 8, 9]
# print(s)
# num = s.count(9)  # считает количество заданных значений в списке
# # print(num)
#
# ind = s.index(9)  # возвращает индекс первого искомого элемента
# print(ind)
# ind = s.index(9, 2)
# print(ind)

