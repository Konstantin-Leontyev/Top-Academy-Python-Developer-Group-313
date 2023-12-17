# Словари

# lst = [1, 2, 3]
# dct = {'one': 1, 'two': 2, 'three': 3}
#
# print(lst[0])
# print(dct['one'])

# dct = {'one': 1, 'two': 2, 'three': 3, 4: 'four'}
#
# dct['one'] = 10
# print(dct['one'])
# print(dct[4])

# d = {}
# print(d)
# print(type(d))
#
# d1 = dict()
# print(d1)
# print(type(d1))
#
# d2 = dict(one=1, two=2)
# print(d2)
# print(type(d2))
#
# d3 = {0: 1, 'two': 2, (1, 2.5): 'кортеж', True: [2, 3, 6, 7], 'two': 45}  # Двух одинаковых ключей быть не может
# print(d)

# d = {0: 1, 'two': 2, (1, 2.3): 'кортеж', True: [2, 3, 6, 7], False: (1, 2)}
# print(d)
# print(d[True][1])
# print(d[(1, 2.3)])
# print(d['two'])
# print(d[0])

# lst = [1, 2, 3]
# lst = [['one', 1], ['two', 2], ['three', 3]]
# d = dict(lst)
# print(d)

# d = {a: a ** 2 for a in range(7)}
# print(type(d))
# print(d)

# d = {'one': 1, 'two': 2, 'three': 3, 4: 'four'}
#
# key = 4
# del d[key]

# if key in d:
#     del d[key]

# try:
#     del d[key]
# except KeyError:
#     print('Элемента с ключом ' + key + ' нет в словаре')
#
# for i in d:
#     print(i, '->', d[i])


# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# composition = 1
# # for key in d:
# #     composition *= d[key]
# for value in d.values():
#     composition *= value
#
# print(composition)


# d = dict()
# d[1] = input('-> ')
# d[2] = input('-> ')
# d[3] = input('-> ')
# d[4] = input('-> ')

# d = {i: input('-> ') for i in range(1, 5)}
# print(d)
#
# dislike = int(input('Какой элемент удалить: '))
# del d[dislike]
# print(d)

# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core-i5-4670K', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core-i5-3450', 5, 6400],
# }
#
#
# for i in goods:
#     print(i, ')', goods[i][0], ' - ', goods[i][1], 'шт. по', goods[i][2], 'руб.', sep=' ')
#
# while True:
#     n = input('№: ')  # 2
#     # if n != '0' and int(n) in range(len(goods) + 1):
#     #     qty = int(input('Количество: '))  # 8
#     #     goods[n][1] += qty
#     # else:
#     #     break
#
#     # if n != '0'
#     #     qty = int(input('Количество: '))  # 8
#     #     try:
#     #         goods[n][1] += qty
#     #     except KeyError:
#     #         ...
#     # else:
#     #     break
#
#     if n != '0':
#         if n in goods:
#             qty = int(input('Количество: '))
#             goods[n][1] += qty
#     else:
#         break
#
#
# for i in goods:
#     print(i, ')', goods[i][0], ' - ', goods[i][1], 'шт. по', goods[i][2], 'руб.', sep=' ')

# d = {'a': 1, 'b': 2, 'c': 3}

# print(d.keys())  # список ключей
# print(d.values())  # список значений
# print(d.items())  # список ключей и значений
#
#
# for key, values in d.items():
#     print(key, '->', values)
#
# print(list(d))

# d = {'a': 1, 'b': 2, 'c': 3}
# # d2 = d
# d2 = d.copy()
# print('d:', d, id(d))
# print('d2:', d2, id(d2))
#
# d2['a'] = 5
# d['e'] = 7
#
# print('d:', d, id(d))
# print('d2:', d2, id(d2))
#
# d.clear()
# print('d:', d, id(d))
# print('d2:', d2, id(d2))

d = {'a': 1, 'b': 2, 'c': 3}

# print(d['e'])
# value = d.get('b', 'Такого элемента не существует')
# print(value)

# item = d.pop('a', 'Такого ключа не существует')  # требует обязательный параметр, второй параметр вернется если элемент не найден
# print(item)
# print(d)


item = d.popitem()
print(item)
print(d)

