# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)

# def func(*args):
#     # print(args)  # (2,)
#     # print(type(args))  # <class 'tuple'>
#     print(*args)
#     print(type(*args))
#     # return args
#
# # print(func(2))
# # print(func(2, 3, 4, 'abc'))  # 2 3 4 abc
# # print(func())

# def summa(*params):
#     res = 0
#     for i in params:
#         res += i
#     return res
#
# print(summa(1,2,3,4,5,6,7,8,9))
# print(summa(3, 4, 5))


# def to_dict(*args):
#     return {element: element for element in args}
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict('greq', (2, 17), 3.11, -4))

# def solution(*args):
#     # print(args)
#     # type(args)
#     avg = sum(*args) / len(*args)
#     print(avg)
#     # print(type(avg))
#     # res = []
#     # for num in args:
#     #     if num < avg:
#     #         res.append(num)
#     # return res
#     return [num for num in tuple(*args) if num < avg]
#
# tpl = 1, 2, 3, 4, 5, 6, 7, 8, 9
# tpl2 = 3, 6, 1, 9, 5
#
# print(solution(tpl))
# print(solution(tpl2))

# def func(a, *args):
#     return a, args
#
# print(func(1))
# print(func())

#
# def print_score(student, *scores):
#     print('Student Name:', student)
#     for score in scores:
#         print(score)
#
#
# print_score('Irina', 5, 4, 3, 2, 5)
# print_score('Igor', 5, 4, 3, 2, 5)
# print_score('Lev')


# def func(*args):
#     # print(args)
#     # print(*args)
#     # print(type(*args))
#     # print(args[0])
#     # print(type(args[0]))
#
#     # print(dir(args))
#     # print(dir(args[0]))
#
#     print(args.__doc__)
#     # print(args[0].__doc__)
#
#     # print(iter(*args))
#
#     # res = []
#     # for element in tuple(*args):
#     #    if element < sum(*args) / len(*args):
#     #        res.append(element)
#     # return res
#     # return [element for element in *args if element < sum(args[0]) / len(*args)]
#
#
# func((1, 2, 3, 4, 5, 6, 7, 8, 9))

# def func(**kwargs):
#     return kwargs
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(d=9))

# def intro(**data):
#     for k, v in data.items():
#         print(k, '->', v)
#     print()
#
# intro(name='Irina', surname='Reznikova', age=22)
# intro(name='Igor', surname='Berukov', email=age=22)


# my_dict = {'one': 'first'}
# print(my_dict)
# print('Внутри функции', id(my_dict))
#
#
# def my_func(**kwargs):
#     my_dict.update(kwargs)
#
#
# my_func(k1=22, k2=31, k3=11, k4=91)
# # print(my_dict)
# # print('С наружи функции', id(my_dict))
#
# my_func(name='Bob', age=31, weight=61, eyes_color='grey')
# print(my_dict)
# print('С наружи функции', id(my_dict))

# def func(a, b, *args, d, e, **kwargs):
#     return a, b, args, e, kwargs, d
#
#
# # print(func(5))
# # print(func(5, 9, 7, 8, 4, 3, 2, 1))
# print(func(5, 9, 7, 8, 4, 3, 2, 1, k1=22, k2=31, k3=11, k4=91, d=55, e=100))

# name = 'Tom'
# print('Глобальная область видимости:', id(name))
#
#
# def hi():
#     global name
#     name = 'Sam'
#     # print('Локальная область видимости:', id(name))
#     surname = 'Johnson'
#     print('Hello', name, surname)
#
#
# def bye():
#     print('Goodbye', name)
#
#
# hi()
# bye()
# print(name)
# # print('Глобальная область видимости:', id(name))

# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()  # 5

# x = 4
#
#
# def add_five(a):
#     x = 2
#
#     def add_some():
#         # x = 1
#         print('x =', x)
#         return a + x
#
#     return add_some()
#
#
# print(add_five(5))
# # add_some()

# sum = 5
#
# lst = [9, 5, 8, 7, 6]
#     print(sum(lst))

# import builtins
#
# name = dir(builtins)
#
# for t in name:
#     print(t)