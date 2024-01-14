def range_check(function):
    """
    Функция декоратор.
    Изменяет введенные пользователем значения местами, если перепутаны местами начало и конец диапазона.
    """
    def wrapper():
        a, b = function()
        if a > b:
            a, b = b, a
        return a, b

    return wrapper


@range_check
def num_input():
    """Инициирует и обрабатывает пользовательский ввод."""
    try:
        # Проверка на ввод не числового значения.
        a, b = map(int, input('Введите коды символов через пробел: ').split())
    except ValueError:
        print('Убедитесь, что введены цифровые значения и повторите ввод')
        a, b = num_input()

    if not all(map(lambda i: i in range(97, 122 + 1), (a, b))):
        print('Убедитесь, что введенные коды находятся в пределах диапазона от 97 до 122 включительно и повторите ввод.')
        a, b = num_input()

    return a, b


a, b = num_input()
print(' '.join([chr(i) for i in range(a, b + 1)]))


