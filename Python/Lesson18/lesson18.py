# from random import randint
#
# SHORTEST = 7
# LONGEST = 10
# MIN_ASCII = 33
# MAX_ASCII = 126
#
#
# def random_password():
#     """Генератор случайных паролей"""
#     random_length = randint(SHORTEST, LONGEST)
#     result = ''.join([chr(randint(MIN_ASCII, MAX_ASCII)) for _ in range(random_length)])
#     return result
#
#
# print('Ваш случайный пароль:', random_password())

# Встроенные функции работы со строками.
# s = 'hello, WORLD! I am Learning Python'

# # Функции регистра строки.
# print(s.capitalize())  # Hello, world! i am learning python
# print(s.lower())  # hello, world! i am learning python
# print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON
# print(s.swapcase())  # HELLO, world! i AM lEARNING pYTHON
# print(s.title())  # Hello, World! I Am Learning Python

# # Подсчет символов в строке.
# # Возвращает количество точных вхождений подстроки в строку.
# print(s.count('h'))  # 2
# # Поиск в заданном диапазоне.
# print(s.count('h', 1, -4))  # 0

# # Поиск индекса.
# # Ищет в строке подстроку и возвращает её индекс.
# # Если не найдено, то возвращает -1.
# print(s.find('Python1'))
# # Поиск в заданном диапазоне.
# print(s.find('Python', 10, -20))
#
# # Поиск первого вхождения с начала строки.
# print(s.find('l'))
# # Поиск первого вхождения с конца строки.
# print(s.rfind('l'))
# # В отличии от find и rfind в случае если вхождение не найдено выбрасывает ValueError
# print(s.index('l'))
# print(s.rindex('l'))

# _s = input('Введите два слова через пробел: ')
# a, b = _s.split()
# a, b = b, a
# _s = ' '.join([a, b])
# print(_s)

# first = _s[: _s.find(' ')]
# second = _s[_s.find(' ') + 1:]
# print(second + ' ' + first)

# # Возвращает True, если строка начинается с указанной подстроки.
# print(s.startswith('hello'))
# print(s.startswith('I am'))  # False
# # Проверка с указанного индекса.
# print(s.startswith('I am', 14))  # True
# # Возвращает True, если строка заканчивается с указанной подстроки.
# print(s.endswith('on.'))
# print(s.endswith('lo.', 3, 5))

# # Проверка содержания.
# # Возвращает True если строка не пустая и не содержит цифр и спец символов.
# # Состоит только из букв.
# print('abc123'.isalpha())  # False
# print('abcABC'.isalpha())  # True
# print(''.isalpha())  # False

# # Проверка содержания.
# # Возвращает True если строка не пустая и не содержит букв и спец символов.
# print('123'.isdigit())  # True
# print('123.234'.isdigit())  # False
#
# # Проверка содержания.
# # Возвращает True если строка не пустая и содержит букв и цифры без спец. символов.
# print('abc123'.isalnum())

# # Проверяет находятся ли символы строки в нижнем регистре.
# # Цифры и спец. символы игнорируются.
# print('abc'.islower())  # True
# print('!abc456'.islower())  # True
# print('!abc456A'.islower())  # False
# # Проверяет находятся ли символы строки в нижнем регистре.
# # Цифры и спец. символы игнорируются.
# print('ABC'.isupper())  # True
# print('!ABC456'.isupper())  # True
# print('!ABC456a'.islower())  # False

# # Выравнивает строку по центру консоли.
# print('py'.center(10, '-'))
# print('py'.center(11, '-'))

# # Удаление пробельных символов.
# # Пробельные символы внутри текста не затрагиваются.
# # С левой стороны.
# print('      p y'.lstrip())
# # С правой стороны.
# print('p y       '.lstrip())
# # И слева и справа.
# print('      p y      '.strip())
#
# print('https://www.python.org'.lstrip())
# print('https://www.python.org'.lstrip('/:pths'))
# print('https://www.python.org'.lstrip('/:pths').rstrip('org'))
# print('https://www.python.org'.strip('/:pthsorg'))

# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# print(str1.replace('N', 'P'))
# print(str1.replace('Nython', 'Python'))
# # Количество заменяемых элементов.
# print(str1.replace('Nython', 'Python', 2))

# s1 = '-'
# seq = ('a', 'b', 'c')
# print(s1.join(seq))
#
# print('..'.join(['1', '2']))
# # print('..'.join([1, 2]))  # Ошибка типа
# print(':'.join('Hello'))

# # Делит строку на список состоящий из подстрок.
# print(s.split())
# print('www.python.org'.split('.'))
# print('www.python.org'.split('.', 1))
# print('www.python.org.ru'.rsplit('.', 2))

# a = input('Введите ФИО: ').split()
# a = ' '.join([a[0].title(), a[1].title()[0] + '.', a[2].title()[0] + '.'])
# print(a)

# a = input('Введите коды символов через пробел: ').split()
# print(a)
#
# b = list(map(int, a))
# print(b)

# Регулярные ворожения.
import re

s = 'Я ищу совпадения в 2024 году. И я их найду в 2 счёта. 987651'
# reg = 'я'
# # findall() - возвращает список содержащий все совпадения,
# # с шаблоном регулярных выражений.
# # Безопасный. Если ничего не найдено вернет пустой список.
# print(re.findall(reg, s))

# # search() - возвращает месторасположение первого совпадения и его конец.
# print(re.search(reg, s).span())
# # Начало совпадения.
# print(re.search(reg, s).start())
# # Конец совпадения.
# print(re.search(reg, s).end())
# # Само совпадение.
# print(re.search(reg, s).group())

# # match() - возвращает месторасположение первого совпадения.
# print(re.match(reg, s))

# reg = r'\.'
# # split() - возвращает список разбитый по шаблону.
# print(re.split(reg, s))
# # sub - метод поиска и замены.
# print(re.sub(reg, '!', s, 1))

# reg = r'2024'  # строгая последовательность цифр.
# reg = r'[204]'  # [] - один из повторяющихся символов.
# reg = r'[0-9]'  # [] - все символы диапазона.
# reg = r'[0-9][0-9][0-9][0-9]'
# reg = r'[12][0-9][0-9][0-9]'
# print(re.findall(reg, s))
# reg = r'[А-Яа-яЁё]'
print(ord('а'))
print(ord('я'))
print(ord('ё'))
print(ord('А'))
print(ord('Я'))
print(ord('Ё'))
# reg = r'[А-яЁё]'
reg = r'[^0-9]'  # все кроме указанных цифр

