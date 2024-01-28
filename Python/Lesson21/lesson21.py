# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res


# def sum_list(lst):  # [3, 5, 7, 9]
#     if len(lst) == 1:
#         print(lst, '=> lst[0]', lst[0])
#         return lst[0]
#     else:
#         print(lst, '=> lst[0]', lst[0])
#         return lst[0] + sum_list(lst[1:])  # 1 + 3
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25


# def to_str(n, base):  # n = 365 // 10 => 36 // 10 => 3
#     convert = '0123456789ABCDEF'
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]  # convert[365 % 10] => convert[5] => 5

# print(to_str(365, 10))
# print(to_str(18, 2))
# print(to_str(18, 8))
# print(to_str(18, 16))


# def to_str(n, base):  # n = 254 // 16 => 14 // 10 => 3
#     convert = '0123456789ABCDEF'
#     if n < base: # 254 < 16; 15 < 16
#         return convert[n]  # convert[15] => F
#     else:
#         return to_str(n // base, base) + convert[n % base]  # convert[14] => E
#
# print(to_str(254, 16))  # FE
# print(to_str(254, 2))  # FE


# names = ['Adam',
#          ['Bob',
#           ['Chat', 'Cat'],
#           'Bart', 'Bert'],
#          'Alex',
#          ['Bea', 'Bill'],
#          'Ann']
#
#
#
# print(names)
# print(len(names))
# print(isinstance(names[0], list))
# print(names[1])
# print(isinstance(names[1], list))

# def count_item(lst):
#     count = 0
#     for item in lst:
#         if isinstance(item, list):
#             count += count_item(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_item(names))

# def remove(text):
#     if not text:
#         return ''
#     if text[0] == '\t' or text[0] == ' ':
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
# print(remove(' Hello\tWorld! '))

# Файлы
# Бинарные файлы

# f = open('lesson21.txt', 'r')
# print(*f)
# print(f.closed)
# print(f)
# f.close()
# print(f.closed)
# print(f.mode)
# print(f.name)
# print(f.encoding)

# f = open('lesson21.txt', 'r')
# # print(f.read())  # Считываем весь файл.
# print(f.read(3))  # Считываем заданное количество символов и переставляет каретку.
# print(f.read())
# f.close()

# f = open('lines.txt', 'r')
# print(f.readline())  # Считывает файл построчно.
# print(f.readline(8))  # Считывает посимвольно и переставляет каретку.
# print(f.readline())  # Досчитывает остаток строки.
# f.close()

# f = open('lines.txt', 'r')
# print(f.readlines())  # Считывать все данные из файла и возвращает список строк.
# print(f.readlines(16)) # Вернет по строку вхождение символа включительно.
# f.close()

# f = open('lines.txt', 'r')
# print(len(f.readlines()))
# f.close()

# f = open('xyz.txt', 'w')
# f.write('Hello\nWorld!\n')
# f.close()

# f = open('xyz.txt', 'a')
# f.write('New text.\n')
# f.close()

f = open('xyz.txt', 'w')
line = ['This is line 1\n', 'This is line 2\n', 'This is line 3\n']
f.writelines(line, )
f.close()
