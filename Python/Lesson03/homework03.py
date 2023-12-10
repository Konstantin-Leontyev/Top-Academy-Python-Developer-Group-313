while True:
    try:
        count = int(input('Введите кол-во символов: '))
        break
    except ValueError:
        print('\nНедопустимое значение.\n'
              'Убедитесь в правильности ввода и повторите попытку.\n')

symbol = input('Введите символ: ')

while True:
    try:
        orientation = int(input('0 - горизонтальная\n'
                                '1 - вертикальная\n'
                                'ориентация линии: '))
        if orientation not in range(-1, 2):
            print('\nНедопустимое значение.\n'
                  'Ориентация задается числами 0 или 1.\n'
                  'Убедитесь в правильности ввода и повторите попытку\n')
            continue
        print(f'{symbol}\n' * count) if orientation else print(symbol * count)
        break
    except ValueError:
        print('\nНедопустимое значение.\n'
              'Ориентация задается числами 0 или 1.\n'
              'Убедитесь в правильности ввода и повторите попытку\n')