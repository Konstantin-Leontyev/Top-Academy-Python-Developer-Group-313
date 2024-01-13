# def mult(t):
#     return t * 2
from random import randint


# lst1 = [2, 8, 12, -5, -10]
# # lst2 = list(map(mult, [2, 8, 12 - 5, -10]))
#
# lst2 = list(map(lambda t: t * 2, lst1))
# print(lst2)
#
#
# t = (2.8, 1,75, 100.55)
# # t2 = tuple(map(lambda x: int(x), t))
# t2 = tuple(map(int, t))
# print(t2)


# t2st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# res = list(map(lambda x, y: (x, y), st, num))
# print(res)

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# res = list(map(lambda x, y: x + y, l1, l2))

# t =('abcd', 'adc, asdfg', 'def', 'grt')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)

# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10))))
# print(m)


# l1 = [randint(1, 40) for _ in range(1, 20)]
# l2 = [x for x in range(10, 20)]
# n = [x for x in l1 if x in l2]
# print(l1)
# print(n)

# my_list = [randint(1,40) for i in range(20)]
#
# print(my_list)
# print(list(filter(lambda num: 10 <= num <= 20, my_list)))

# def hello():
#     return 'hello, I am func "hello"'
#
#
# def super_func(func):
#     print('hello, I am func "super_func"')
#     print(func())
#
#
# super_func(hello)

# def hello():
#     return 'hello, I am func "hello"'
#
#
# test = hello
# print(test())

# def my_decorator(func):
#     def wrap():
#         print('*' * 30)
#         func()
#         print('*' * 30)
#     return wrap
#
# @my_decorator  # декоратор
# def func_test():  #  декорируемая функция
#     print('Hello, I am func "func_test"')
#
#
# func_test()
# # test = my_decorator(func_test)
# # test()


# def bold(fn):
#     def wrap():
#         return '<b>' + fn() + '<b>'
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return '<i>' + fn() + '<i>'
#
#     return wrap
#
# @bold
# @italic
# def hello()
#     return 'text'
#
# print(hello())

# def cnt(fn):
#     count = 1
#
#     def wrap():
#         fn()
#         nonlocal count
#         print(f'Вызов функции: {count}')
#         count = count + 1
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()

# def cnt(fn):
#     count = 1
#
#     def wrap(arg1, arg2):
#         nonlocal count
#         print('Вызов функции:', count, '\n', '*' * 20, end='')
#         fn(arg1, arg2)
#         count = count + 1
#
#     return wrap
#
#
# @cnt
# def hello(a, b):
#     print('\nHello', a, '\nHello,', b)
#
#
# hello('Python', 'JavaScript')
# hello('one', 'two')

# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print('args', args)
#         print('kwargs', kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def print_data(a, b, c, study='Python'):
#     print(a, b, c, 'изучают', study, '\n')
#
#
# print_data('Борис', 'Елизовета', 'Светлана', study='JavaScript')
# print_data('Владимир', 'Екатерина', 'Виктор')

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, '=', end=' ')
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
# @decor("Сумма", '+')
# def summa(a, b):
#     print(a + b)
#
#
# @decor('Разность', '-')
# def sub(a, b):
#     print(a - b)
#
# summa(5, 2)
# sub(6, 4)


def multiply(arg):
    def test(fn):
        def wrap(x):
            return fn(x) * arg

        return wrap

    return test


@multiply(5)


def return_num(num):
    return num


print(return_num(5))
