month = int(input("Введите номер месяца (цифрой): "))
if month not in range(1, 13):
    print("Ошибка ввода данных")
elif month in range(3, 6):
    print("Время года - весна")
elif month in range(6, 9):
    print("Время года - лето")
elif month in range(9, 12):
    print("Время года - осень")
else:
    print("Время года - зима")
