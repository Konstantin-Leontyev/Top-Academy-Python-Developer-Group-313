# Я несколько раз пересмотрел конец занятия.
# И не понял, в чем невозможность решения при итерации по элементам.
# Мы без проблем можем зайти через встроенный метод списка
# и получить индекс элемента и потом с ним играть как угодно.

# # numbers = [int(input('-> ')) for _ in range(int(input('n =')))]
# numbers = [2, 9, 4, 6, 3, 5]
# for number in numbers:
#     index = numbers.index(number)
#     # if index == 0:
#     #     continue
#     # elif number > numbers[index - 1]:
#     #     print(number, end=' ')
#
#     if index != 0 and number > numbers[index - 1]:
#         print(number, end=' ')
#
# Оказывается можно еще через срез зайти и условие сократить
# numbers = [2, 9, 4, 6, 3, 5]
# for number in numbers[1: len(numbers)]:
#     # index = numbers.index(number)
#     # if number > numbers[index - 1]:
#     #     print(number, end=' ')
#     if number > numbers[numbers.index(number) - 1]:
#         print(number, end=' ')

# Задание 1 Вариант 1
# numbers = [int(input('-> ')) for _ in range(int(input(''Введите количество элементов списка: ')))]
# numbers = [6, 3, 0, 8, 2]
# # Не прибегая к циклу (не оптимальный вариант)
# # Так как мы бегаем по списку в каждой строке
# # Скорость работы будет расти в прогрессии размера списка
# sum_of_numbers = sum(numbers)  # сразу считаем сумму (нули нам не мешают)
# count_of_zero = numbers.count(0)  # считаем количество нулей в списке
# count_of_numbers = len(numbers) - count_of_zero  # количество элементов кроме нулей
# average = sum_of_numbers / count_of_numbers  # среднее значение
# print('Средне арифметическое: ', average)

# Задание 1 Вариант 2
# numbers = [int(input('-> ')) for _ in range(int(input(''Введите количество элементов списка: ')))]
# numbers = [6, 3, 0, 8, 2]
# в этом варианте мы пробегаем по списку всего один раз
# заходить через индексы при решении этой задачи считаю иррациональным
# sum_of_numbers = 0
# count_of_numbers = 0
#
# for number in numbers:
#     if number != 0:
#         sum_of_numbers += number
#         count_of_numbers += 1
#
# average = sum_of_numbers / count_of_numbers  # среднее значение
# print('Средне арифметическое: ', average)

# # Задание 2 вариант 1
# numbers = [5, 1, 9, 7, 6, 3]
# for number in numbers:
#     if numbers.index(number) % 2 == 0:
#         print(number, end=' ')

# # Задание 2 вариант 2
# не знаю как внутри устрое метод index()
# но думаю он перебирает значения
# потому с точки зрения производительности
# лучше вариант где мы в ручную перебираем значения
# numbers = [5, 1, 9, 7, 6, 3]
# for i in range(len(numbers)):
#     if i % 2 == 0:
#         print(numbers[i], end=' ')
