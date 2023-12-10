import random

randInt = random.randint(1, 101)
count = 0
print('\t\t\t\t----- Игра угадай число ----\n')

while True:
    while True:
        count += 1
        num = input('Введите целое число от 1 до 100 (для выхода из программы введите 0): ')

        while type(num) is not int:
            try:
                num = int(num)
            except:
                num = input('Введено не целое число!. '
                            'Введите целое число от 1 до 100 (для выхода из программы введите 0): ')

        if num == randInt:
            print('\nВы угадали загаданное число c', count, 'раза')
            break
        elif not num:
            print('Работа программы завершена')
            break
        elif num < randInt:
            print('Загаданное число больше ')
        else:
            print('Загаданное число меньше ')

    if not num:
        break
    else:
        out = input('\nСыграем еще? (Y/N): ')
        match out:
            case 'Y' | 'y':
                continue
            case 'N' | 'n':
                print('Работа программы завершена')
                break
