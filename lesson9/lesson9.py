# def digit_sum(n, is_even=True):
#     # s = 0
#     # while n > 0:
#     #     current = n % 10
#     #     if is_even and current % 2 == 0:
#     #         s += current
#     #     if not is_even and current % 2 != 0:
#     #         s += current
#     #     n //= 10
#     # return s
#     nums = [int(num) for num in str(n)]
#     res = 0
#     for num in nums:
#         if is_even and num % 2 == 0:
#             res += num
#         elif not is_even and num % 2 != 0:
#             res += num
#
#     return res
#
#
# print('Сумма четных цифр:')
# print(digit_sum(9874023, is_even=True))
# print(digit_sum(38271, is_even=True))
# print(digit_sum(123456789, is_even=True))
# print('\nСумма нечетных цифр:')
# print(digit_sum(9874023, is_even=False))
# print(digit_sum(38271, is_even=False))
# print(digit_sum(123456789, is_even=False))

# def display_info(name, age):
#     print('Name:', name, '\nAge', age)
#
#
# display_info('Ira', 23)
# display_info(23, 'Ira')
# display_info(age=23, name='Ira')
# display_info('Igor', age=23, name='Ira') # TypeError

# Изменяемые и неизменяемые объекты

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(id(lt1))
# print(id(lt2))
# print(id(lt1[0]))
# print(id(lt1[0]))
# print(lt1 == lt2)  # True
# print(lt1 is lt2)  # False
#
# a = 'Hello'
# b = 'Hello'
# print(id(a))
# print(id(b))
# print(id(lt2))
# print(a == b)  # True
# print(a is b)  # True
#
# n = 5
# m = 5
# print(id(n))
# print(id(m))
# print(n == m)
# print(m is n)

# n = 5
# print(id(n))
# n = 6
# print(id(n))
#
# n = 'Hello'
# print(id(n))
# n = 'Python'
# print(id(n))

# n = [1, 2, 3]
# print(id(n))
#
# n.append(4)
# print(n)
# print(id(n))

# Кортеж (tuple)
# n = (1, 2, 3)
# print(id(n))
#
# n.append(4)
# print(n)
# print(id(n))

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())  # 72
# print(tpl.__sizeof__())  # 48

# # a = ()
# a = 5, 9, 7, 8
# # b = tuple()
# print(type(a))
# # print(type(b))
# print(a)
# # print(b)

# # a = (5)
# # a = 5,
# a = (5,)
# print(type(a))
# print(a)

# n = [1, 2, 3]
# b = tuple(n)
# print(type(b))
# print(b)

# n = 'Hello', 'Python'
# b = tuple(n)
# print(type(b))
# print(b)

# a = (1, 2, 3, 4, 5, 6)
# print(a)
# print(a[3])  # 4
# print(a[1:3])  # (2, 3)
# # a[1] = 3  # не работает - typeError

# s = [i for i in range(5)]
# print(s)
#
# x = tuple(i for i in range(5))
# print(x)
#
# z = {i for i in range(5)}
# print(z)

from random import randint

# s = tuple(int(input('->')) for i in range(5))
# s = tuple(randint(0, 100) for i in range(5))
# print(s)

# s = tuple(2 ** i for i in range(1, 13))
# print(s)

# t1 = tuple('hello')
# t2 = tuple('world')
# print(t1)
# print(t2)
# t3 = t1 + t2
# print(t3)
# # print(t1 * 2)
# # t4 = list(t3)
# print(t3.count('a'))
# # print(t3.index('l', 3))  #
# # print(t3.index('l', 4, -2))  #
# # if 'e' in t3:
# #     print(t3.index('e'))
#
# # for i in t3:
# #     print(i, end=' ')

# t1 = (1, 2, 3)
# t2 = (1, 8, 3, 4, 8, 8, 9, 2)
# t3 = (1, 2, 8, 5, 1, 2, 9)
#
#
# def slicer(tpl: tuple, num: int) -> tuple:
#     if num not in tpl:
#         return ()
#     else:
#         if tpl.count(num) > 1:
#             start_index = tpl.index(num)
#             stop_index = tpl.index(num, start_index + 1)
#             return tpl[start_index: stop_index + 1]
#         else:
#             return tpl[tpl.index(num):]  # tpl[2:]
#
#
# print(slicer(t1, 8))
# print(slicer(t2, 8))
# print(slicer(t3, 8))


# t = (10, 11, [1, 2, 3], [3, 4, 5], ['hello', 'world'])
# print(t, id(t))
# t[4][0] = 'new'
# print(t, id(t))
# t[4].append('hi')
#
# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
#
# x, y, z = t  # распаковка
# # x, y = t # работать не будет - недостаточно элементов для распаковки
# # x, y, z, q = t # работать не будет - слушком много элементов для распаковки
#
# print(x, y, z)


def get_user():
    name = 'Tom'
    age = 22
    is_married = False
    return name, age, is_married


user = get_user()
# print(user)
# print(user[0])
# print(user[1])
# print(user[2])
# first_name, age, is_married = user
first_name, age, is_married = get_user()
print(first_name, age, is_married)


