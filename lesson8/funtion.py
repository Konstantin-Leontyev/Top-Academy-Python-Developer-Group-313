# Function

# def hello():
#     print('Hello')
#
#
# hello()

# def hello(name):  # name - аргумент функции
#     print('Hello,', name)
#
#
# hello('Irina')  # Параметры
# hello('Igor')


# def getSum(a, b):  # не рекомендуется именовать функции в кэмел кейсе
# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5

# get_sum(2, 5)
# get_sum(x, y)
# get_sum('adc', 'def')

# def symbol(count, a, b):
#     ...
#
#
# symbol(9, '+', '-')
# symbol(9, 'X', '0')

# def get_sum(a, b):
#     print('Сумма: ', end='')
#     return a + b
#
#
# x = 2
# y = 5
#
# res = get_sum(2, 5)
# print(res)

# def get_maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(9, 16)

# a = int(input('Введите а: '))
# b = int(input('Введите b: '))
#
#
# def function(x, y):
#     if a > b:
#         return a - b
#     else:
#         return a + b
#
#
# print('Результ:', function(a, b))

# def cube(a):
#     str = ''
#     for i in range(0, a + 1):
#         str += f'{i} в кубе = {i ** 3}\n'
#     return str
#
#
# res = cube(10)
#
# print(res)

# def change(lst):
#     lst = list(lst)
#     # print(lst)
#     # symbol1 = lst.pop(0)
#     # symbol2 = lst.pop(-1)
#     # lst.insert(0, symbol2)
#     # lst.append(symbol1)
#     # print(lst)
#
#     lst[0], lst[-1] = lst[-1], lst[0]
#     print(lst)
#
#
# change('слон')


# def is_greater(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# a = 10
# b = 5
#
# print(is_greater(a, b))
# print(is_greater(b, a))
#
#
# if is_greater(a, b):
#     print(a, 'больше', b)

def check_password(password):
    has_upper = False
    has_lower = False
    has_num = False

    for ch in password:
        if 'A' <= ch <= 'Z':
            has_upper = True
            break

    for ch in password:
        if 'a' <= ch <= 'z':
            has_lower = True
        elif 'a' <= ch <= 'z':
            has_lower = True
        elif '0' <= ch <= '9':
            has_num = True

    if len(password) >= 8 and has_upper and has_lower and has_num:
        return True
    return False


p = input('Введите пароль: ')

if check_password(p):
    print('Это надежный пароль')
else:
    print('Это не надежный пароль')
