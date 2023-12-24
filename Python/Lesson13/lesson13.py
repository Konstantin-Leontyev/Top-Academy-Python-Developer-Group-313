

# d1 = {'r': 7, 'q': 40}
# d.update(d1)
# d2 = [('a', 20), ('b', 9)]
#
# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}

# new_dict = x.copy()
# new_dict.update(y)
# new_dict = x | y
# print(new_dict)

# a = {
#     'first': {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'second': {
#         4: 'four',
#         5: 'five'
#     }
# }
#
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t', y, ':', a[x][y], sep='')

# sales = {
#     'John': {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
#     'Tom': {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
#     'Anne': {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
#     'Fiona': {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451}
# }
#
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print('\t', y, ':', sales[x][y], sep='')
#
# person = input('Имя: ')
# region = input('Регион: ')
# print(sales[person][region])
# new_date = int(input('Новое значение: '))
# sales[person][region] = new_date
#
# print(sales[person])

# d = {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694}
# print(d)
# new_date = {value: key for key, value in d.items()}
# print(new_date)
#
# d.update({value: key for key, value in d.items()})
# print(d)

# d = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# new_d = {k: v for k, v in d.items() if v <= 2}

# print('Начальный словарь')
# c = list(d)
# for key in c[:2]:
#     print(f'{key}: {d[key]}')

# c = list(d.items())[:2]
# for key, value in c:
#     print(f'{key}: {value}')

# for key, value in list(d.items())[2:4]:
#     print(f'{key}: {value}')

# list = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
#
# d = {}
#
# curren_key = ''
# for item in list:
#     if type(item) == str:
#         d[item] = []
#         curren_key = item
#     else:
#         d[curren_key].append(item)
#
# print(list)

# d = dict([(1, 'one'), (2, 'two'), (3, 'three')])
# d = dict(zip([1, 2, 3], ['one', 'two', 'three']))
# print(d)

# a = [1, 2, 3]
# b = ['one', 'two', 'three']
# f = {k: v for k, v in zip(a, b)}


# a = [1, 2, 3]
# b = ['one', 'two', 'three']
# d = [4.5, 7.4, 9.6]
# c = tuple(zip(a, b))
# print(c)
# # c = list(zip(a, b))
# c = list(zip(a, b, d))
# # print(c)
# # c = set(zip(a, b))
# # print(c)
# # c = dict(zip(a, b, d))
# print(c)

d_one = {'name': 'Igor', 'last_name': 'Petrov', 'Job': 'Software Engineer'}
d_two = {'name': 'Irina', 'last_name': 'Irisova', 'Job': 'Manager'}

for (k1, v1), (k2, v2) in zip(d_one.items(), d_two.items()):
    print(k1, v1, k2, v2)

d = [(1, 'one'), (2, 'two'), (3, 'three')]
a, b = zip(*d)
print(a)  # (1, 2, 3)
print(b)  # ('one', 'two', 'three')

# a = ['two', 'one', 'three']
# b = [3, 2, 1]
# a = list(zip(a, b))
# print(a)  # [('two', 3), ('one', 2), ('three', 1)]
#
# b.sort()
# print(b)
# print(dict(b))

# one = {'apple': 0.45, 'orange': 0.35, 'pepper': 0.5}
# two = {'pepper': 0.2, 'onion': 0.55}
# print({**one, **two})  # {'apple': 0.45, 'orange': 0.35, 'pepper': 0.2, 'onion': 0.55}

# print({**two, **one})  # {'pepper': 0.5, 'onion': 0.55, 'apple': 0.45, 'orange': 0.35}
#
# for k, v in {**two, **one}.items():
#     print(f'{k} = {v}')
    # Вывод:
    # pepper = 0.5
    # onion = 0.55
    # apple = 0.45
    # orange = 0.35

# data = ['red', 'blue', 'green', 'yellow', 'orange']
# num = 1
# for val in data:
#     print(num, ')', val, sep='')
#     num += 1
#
# print()
# for num, val in enumerate(data, 1):
#     print(num, ')', val, sep='')
