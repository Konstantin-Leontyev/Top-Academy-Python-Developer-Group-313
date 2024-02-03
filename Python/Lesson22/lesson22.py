# f = open('xyz.txt', 'w')
# lst = [i for i in range(1, 20)]
# print(lst)
#
# for index in lst:
#     f.write(str(index) + '\t')
# f.close()

# f = open('text.txt', 'w')
# f.write('Замена строки в текстовом файле;\n'
#         'изменить строку в списке;\n'
#         'записать список в файл;\n'
#         )
# f.close()
#
# f = open('text.txt', 'r+')
# rl = f.readlines()
# rl[1] = 'Hello world!\n'
# f.close()
#
# f = open('text.txt', 'w')
# f.writelines(rl)
# f.close()

#
# def input_index():
#     file = open('text.txt', 'r')
#     read_text = file.readlines()
#     file.close()
#     index = int(input('Введите номер строки: '))
#     if index not in range(1, len(read_text) + 1) or index < 1:
#         print('Убедитесь что введен корректный номер строки и повторите попытку.')
#         return input_index()
#     else:
#         return read_text, index - 1
#
#
# t, i = input_index()
#
# f = open('text.txt', 'w')
# del t[i]
# f.writelines(t)
# f.close()

# f = open('test.txt', 'r')
# print(f.read(3))
# print(f.tell())  # возвращает текущую позицию условного курсора в файл
# print(f.seek(1))
# print(f.read())
# print(f.tell())
# f.close()

# f = open('test.txt', 'a+')
# print(f.write('I\'m learning Python'))
# print(f.tell())
# print(f.seek(3))
# print(f.write('-new string-'))
# print(f.tell())
# f.close()

# with open('test.txt', 'w+') as f:
#     print(f.write('01234\n56789'))
#
# with open('test.txt', 'r') as f:
#     for line in f:
#         print(line[:3])

# file_name = 'res_1.txt'
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     # lt = list(map(str, lt))
#     lt = list(map(str, lt))
#     print(lt)
#     print(type(lt))
#     return ' '.join(lt)
#
#
# with open(file_name, 'w+') as f:
#     # f.write(str(lst))  # [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#     f.write(get_line(lst))  # [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# with open(file_name, 'r') as f:
#     numbers = f.read()
#
# print(numbers)  # 4.5 2.8 3.9 1.0 0.3 4.33 7.777
#
# num_list = list(map(float, numbers.split()))
# print(num_list)
# print(type(num_list))
# print(sum(num_list))
# print(len(num_list))
#
# print('Done')

# def longest_worlds(file):
#     with open(file, 'r') as text:
#         text = text.read().split()
#         max_length = len(max(text, key=len))
#         res = [word for word in text if len(word) == max_length]
#         return res
#
#
# print(longest_worlds('task.txt'))

one = 'one.txt'
two = 'two.txt'

# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"
# with open(one, 'w') as f:
#     f.write(text)

with open(one, 'r') as first, open(two, 'w') as second:
    for line in first:
        line = line.replace('Строка', 'Линия -')
        second.write(line)
