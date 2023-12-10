# a = [1, 2, 3]
# b = a.copy()  # возвращает копию списку
# print('a =', a)
# print('b =', b)
# a.append(20)
# print('a =', a)
# print('b =', b)
# b.append(120)
# print('a =', a)
# print('b =', b)

# a = [5, 4, 1, 2, 3]
# print('a =', a)
# a.reverse() # перестраивает элементы списка в обратном порядке
# print('a =', a)
#
# a.sort()  # сортировка элементов списка
# print('a =', a)
# a.sort(reverse=True)  # сортировка элементов списка в обратном порядке
# print('a =', a)

# b = ['Виталий', 'Сергей', 'Александр', 'Анна']
# # b.sort()
# # print(b)
# # b.sort(key=len)
# # print(b)
# b.sort(key=len, reverse=True)
# print(b)

# a = [5, 4, 1, 2, 3]
# print('a =', a)
# print(id(a))
# a.sort()
# print(id(a))
# sort = sorted(a)
# print(sort)
# print(id(sort))

# Генерация случайных данных

# from random import random, randint, randrange, uniform, choice, choices, shuffle
#
# print(random())
# print(randint(0, 9))  # от 3 по 9 (включительно)
# print(randrange(0, 9))  # от 3 до 9 (не включительно)
#
# print(uniform(10.5, 25.5))
# print(round(uniform(10.5, 25.5), 2))
#
# city_list = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# # print(choice(city_list))
# # print(choices(city_list, k=3))
# shuffle(city_list)
# print(city_list)
#
#
# s = [55, 66, 77, 88, 99, 9, 8, 7, 6, 5, 4, 1, 2, 3]
# # print(choice(s))
# print(choices(s, k=5))


# lst = [5, 4, 3, 2, 1]
# # lst = ['5', '4', '3', '2', '1']
# print(len(lst))
# print(sum(lst))
# print(max(lst))
# print(min(lst))

# from random import randint
# lst = [randint(0, 100) for i in range(10)]
# print(lst)
# # m = max(lst)
# # i = lst.index(m)
# # print(m)
# # m = lst.pop(i)
# # lst.insert(0, m)
# lst.insert(0, lst.pop(lst.index(max(lst))))
# print(lst)

# from random import randint
# lst = [randint(0, 100) for i in range(10)]
# print(lst)
#
# m = min(lst)
# print(m)
# index = lst.index(m)
# del lst[: index]
# print(lst)

# x = list('1a2b3c4d')
# print(x)
# print('a' in x)
# print('e' in x)
#
# print('a' not in x)
# print('e' not in x)

# lst = []
# # print(bool(lst))
# # if len(lst) == 0:
# if not lst:
#     print('Список пустой')
# else:
#     print('В списке есть элементы')

# if lst:
#     print('В списке есть элементы')
# else:
#     print('Список пустой')

# len1 = int(input('Введите размер первого списка: '))
# len2 = int(input('Введите размер второго списка: '))

# from random import randint
# 
# lst1 = [randint(0, 10) for i in range(len1)]
# lst2 = [randint(0, 10) for j in range(len2)]
# 
# print('Первый список', lst1)
# print('Второй список', lst2)
# # lst3 = lst1.extend(lst2)
# # lst3 = lst1 + lst2
# # print('Третий список', lst3)
# # lst4 = [element for element in lst3 if lst3.count(element) == 1]
# # print('Четвертый список', lst4)
# 
# lst3 = []
# for element in lst1:
#     if element in lst2 and element not in lst3:
#         lst3.append(element)
# print('Элементы общие для двух списков', lst3)

m = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     ]
print(m)
print()
# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col], end='\t')
#     print()

for row in m:
    for element in row:
        print(element, end='\t')
    print()
    