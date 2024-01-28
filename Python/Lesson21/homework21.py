data = [0, -2, 3, 9, -11, -4, -5, 6, 7, 7, -1]


def count_negative(lst: list) -> int:
    count = 0
    if not lst:
        return count
    # Вот тут долго мучался над оптимизацией.
    # Дело в том, что условием рекурсивного вызова служит положительное число.
    # В этом смысле сдвигаться на одно число значит повторно его проверять.
    # Я перехожу к проверке сразу следующего числа. Начиная новый список с него.
    # При этом подходе смещение по вновь передаваемому списку происходит сразу на несколько индексов.
    for i in range(1, len(lst) + 1):
        if lst[i - 1] < 0:
            count += 1
        else:
            return count + count_negative(lst[i:])
    return count


print(count_negative(data))