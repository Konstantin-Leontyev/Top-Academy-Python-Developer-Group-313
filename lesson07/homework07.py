from random import randint, choice

# Спрашиваем у пользователя длину списка
list_len = int(input('Ведите длину списка: '))
# Создаем список для заполнения
lst = []

# Вариант 1
# # До тех пор пока список не будет заполнен
# while len(lst) != list_len:
#     # Генерируем случайный элемент
#     element = randint(1, list_len)
#     #  если его еще нет в списке
#     if element not in lst:
#         # заносим его в список
#         lst.append(element)
#
# # Печатаем его в консоль
# print(lst)

# Вариант 2 (без особых преимуществ)
# Заполняем список значениями от 1 до длины списка
num_list = [i for i in range(list_len)]

# Пока не заполниться список
while len(lst) != list_len:
    # Выбираем элемент из списка num_list
    element = choice(num_list)
    #  если его еще нет в списке
    if element not in lst:
        # заносим его в список
        lst.append(element)

# Печатаем его в консоль
print(lst)

