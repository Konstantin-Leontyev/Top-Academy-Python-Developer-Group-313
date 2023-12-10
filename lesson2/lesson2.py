# num = 4321
# a = num % 10
# b = (num // 10) % 10
# c = (num // 100) % 10
# d = (num // 1000) % 10
# print(a)
# print(b)
# print(c)
# print(d)
#
# num = a * 1000 + b * 100 + c * 10 + d
# print(num)

# num = 4325  # => 5234
# print("Исходное число:", num)
# res = num % 10 * 1000
# num //= 10
# res += num % 10 * 100
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print("Развернутое число:", res)

# num1 = "2.3"
# num2 = 3
# # res = num1 + str(num2)
# res = int(num1) + num2
# res = float(num1) + num2
# print(res)

# print(int(3.8))
# print(round(3.8))
# print(type(round(3.8)))
# print(round(3.891, 2))
# print(type(round(3.891, 2)))

# name = "Виктор"
# age = 28
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут", name, ". Мне", str(age), "лет.")
# print("Меня зовут", name, ". Мне", str(age), "лет.", sep="$$$$$$")
# print(f"Меня зовут, {name}. Мне {str(age)}, лет.", end=" ")
# print("Я учу Python")

# name = input("Введите имя: ")
# print(name)

# num = input("Введите число: ")
# power = input("Введите степень: ")
# res = int(num) ** int(power)

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# res = num ** power
# print("Число", num, "в степени", power, "равно", res)

# b1 = True
# b2 = False
# print(b1 + 5)  # 1 + 5
# print(b2 + 5)  # 0 + 5

# print(bool("python"))  # True
# print(bool(""))  # False
# print(bool(-0.2))  # True
# print(bool(0))  # False
# print(bool(False))  # False
# print(bool(None))  # False
#
# test = None
# print(test)

# print(7 == 7)
# print(7 == "7")
# print(5 + 2 == 7)
# print(7 != 10 - 7)
# print(8 > 5)
# print(8 < 5)
# print(9 <= 9)
# print(9 >= 9)
# print("привет" > "ПРИВЕТ")

# print(2 < 4 < 9)  # 2 < 4 < 9 True && True
# print(2 * 5 > 7 >= 4 + 3)  # True
# print(3 * 3 <= 7 >= 2)  # False && True => False

# a = 10
# b = 5
# c = a == b
# print(a, b, c)  # 10 5 False

# print(5 - 3 == 2 and 1 + 3 == 4)  # True (True:True)
# print(5 - 3 == 2 and 1 + 3 < 4)  # False (True:False)
# print(5 - 3 > 2 and 1 + 3 == 4)  # False (False:True)
# print(5 - 3 > 2 and 1 + 3 < 4)  # False (False:False)

# print(5 - 3 == 2 or 1 + 3 == 4)  # True (True:True)
# print(5 - 3 == 2 or 1 + 3 < 4)  # True (True:False)
# print(5 - 3 > 2 or 1 + 3 == 4)  # True (False:True)
# print(5 - 3 > 2 or 1 + 3 < 4)  # False (False:False)

# print(9 - 7)
# print(not 9 - 7)
# print(not 7 - 7)

# cnt = 5
# if cnt < 10:
#     cnt += 2
#     print(cnt)


# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("доступ на сайт разрешен: ")
# else:
#     print("Доступ запрещен")

# a = 15
# b = 5
# if a > b:
#     print("a > b")
# elif a < b:
#     print("a < b")
# else:
#     print("a = b")

# side1 = int(input("Введите сторону 1: "))
# side2 = int(input("Введите сторону 2: "))
# side3 = int(input("Введите сторону 3: "))
#
# if side1 == side2 == side3:
#     print("Треугольник равносторонний")
# elif side1 == side2 or side1 == side3 or side2 == side3:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")

# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5)
#     print("Рабочий день - ")
# elif day == 6 or day == 7:
#     print("Выходной день - ")
# else:
#     print("Такого дня недели не существует")

# day = int(input("Введите день недели (цифрой): "))
# if day in range(1, 6):
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day in range(6, 8):
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели не существует")

# month = int(input("Введите номер месяца (цифрой): "))
# if month not in range(1, 13):
#     print("Ошибка ввода данных")
# elif month in range(3, 6):
#     print("Время года - весна")
# elif month in range(6, 9):
#     print("Время года - лето")
# elif month in range(9, 12):
#     print("Время года - осень")
# else:
#     print("Время года - зима")
