# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print(a + b)
#
#     print('a: ', a)
#     fun2(4)
#
#
# fun1()

# x = 25
# t = 0
#
#
# def fb():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a
#         a = 35
#         print('a: ', a)
#
#     inner()
#     t = a
#
#
# fb()
# c = x + t
# print(c)


# def fn1():
#     x = 25
#
#     def fn2():
#         x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print('fn2.x = ', x)
#
#     fn2()
#     print('fn1.x = ', x)
#
#
# fn1()

# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# res = outer(2, 3, -1, 4)
# print(res)

# Замыкания
#
# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
# item1 = outer(5)
# print(item1(10))
#
# item2 = outer(5)
# print(item2(1))
# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         # nonlocal a
#         # c.append(4)
#         # a = a + 1
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())

# def func(city):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return inner
#
#
# res1 = func('Москва')
# print(res1(), id(res1))
# print(res1(), id(res1))
# res2 = func('Сочи')
# print(res2(), id(res2))
# print(res2(), id(res2))
# print(res2(), id(res2))
# print(res1(), id(res1))
# lambda (анонимная функция)

# print((lambda x, y: x + y)(1, 2))
#
# func = lambda x, y: x + y
# print(func(1, 2))
#
# print((lambda x, y: x ** 2 + y ** 2)(2,5))
# print((lambda x, y=5: x ** 2 + y ** 2)(2))
# print((lambda x=2, y=5: x ** 2 + y ** 2)())

# print((lambda *args: args)(1, 2, 3, 4, 5))
#
# y = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# )
#
# for i in y:
#     print(i('abc__'))

# def outer(n):
#     def inner(x):
#         return x + n
#
#     return inner
#
# f = outer(5)
#
# print(f(10))

# def outer(n):
#     return lambda x: x + n
#
#
# f = outer(5)
# print(f(10))


# outer = lambda n: lambda x: x + n
#
#
# f = outer(5)
# print(f(10))

# print((lambda n: lambda x: x + n)(5)(10))
# print((lambda n: lambda x: lambda y: x + n + y)(2)(4)(6))

# def func(item):
#     return item[1]
#
# d = {'b': 3, 'c': 1, 'a': 2}
# print(d)
# lst = list(d.items())
# print(lst)
# lst.sort(key=func)
# lst.sort(key=lambda i: i[1])
# print(lst)
# d1 = dict(lst)
# print(d1)
#
# players = [
#     {'name': 'Антон', 'last_name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last_name': 'Бодня', 'rating': 10},
#     {'name': 'Федор', 'last_name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last_name': 'Семенов', 'rating': 6},
# ]
#
# res = sorted(players, key=lambda item: item['last_name'])
# print(res)
# res = sorted(players, key=lambda item: item['rating'], reverse=True)
# print(res)

# d = {
#     1: lambda: print('Понедельник'),
#     2: lambda: print('Вторник'),
#     3: lambda: print('Среда'),
#     4: lambda: print('Четверг'),
#     5: lambda: print('Пятница'),
#     6: lambda: print('Суббота'),
#     7: lambda: print('Воскресенье')
# }
#
# d[6]()

# print((lambda a, b: a if a > b else b)(15, 23))

print((lambda a, b, c: a if (a < b and a < c) else (b if b < c else c))(28, 29, 27))

