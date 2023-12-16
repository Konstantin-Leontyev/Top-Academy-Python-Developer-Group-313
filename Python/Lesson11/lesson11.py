# # Множества (set)
#
# s = {'banana', 'apple', 'orange', 'banana', 'apple'}
# print(s)
# print(type(s))
# print(len(s))
#
# # a = {}
# # a = set()
# a = set('hello')
# print(a, type(a))

# c = ['red', 'blue', 'green', 'red']
#
# a = set(c)
# print(a, type(a))

# mas = [1,2,3,2, 3, 4, 4, 5}
# s = {x for x in range(10)}
# print(s)

# def to_set(data):
#     tmp_set = set(data)
#     return tmp_set, len(tmp_set)
#
#
# test_str = 'я обычная строка'
# test_list = [4, 5, 4, 6, 2, 9, 11, 3, 4, 2]
# print(to_set(test_str))
# print(to_set(test_list))

# t = {'red', 'green', 'blue'}
# print('green' in t)
# for i in t:
#     print(i)

# r = ['ad_1', 'ac_2', 'bc_3', 'bc_2']
# # a = [i for i in r if 'a' not in i]
# # a = ['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r]
# a = ['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if i[1] == 'c']
# print(a)


# a = {'Tom', 'Bob', 'Alice'}
# print(a)
# a.add('Ann')
# print(a)
# # a.remove('Ann')  # при обращении к несуществующему элементу - ошибка KeyError
# # print(a)
# # user = 'Anna'
#
# # a.pop()  # удаляет первый элемент
# n = a.pop('Tom')  # возвращяет удаляемый элемент
# print(n)
# print(a)

a = {0, 1, 2, 3}
b = {4, 3, 2, 1}
# c = a.union(b)  # c = a | b
# print(c)
# a.update(b)  # a | = b
# c = a.intersection(b)  # c = a & b
# a.intersection_update(b)  # a &= b
# c = difference(b)  # c = a - b
# a.difference_update(b)  # a -= b
# c = a ^ b
# a ^= b
# print(c)
# print(a)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# # s = s1.union(s2, s3, s4, s5, s6, s7)
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# count = len(s)
# print('Count: ', count)
# print('Minimum: ', min(s))
# print('Maximum: ', max(s))
# print('Summary: ', sum(s))

# s1 = 'Hello'
# s2 = 'How are you'
#
# s3 = set(s1) & set(s2)
# print(*s3)

# drawing = {'Марина', 'Женя', 'Света'}
# music = {'Костя', 'Женя', "Илья"}
# one_hobby = drawing ^ music
# both_hobbies = drawing & music
# drawing -= both_hobbies
#
# print('Одно хобби:', one_hobby)
# print('Оба кружка:', both_hobbies)
# print('Кружок рисования:', drawing)

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# print(a <= b)
# print(a >= b)


# Тип frozenset
# s = frozenset([1, 2, 3, 4, 5])
# print(s)
# print(type(s))
# a = frozenset({'hello', 'world'})
# print(a)