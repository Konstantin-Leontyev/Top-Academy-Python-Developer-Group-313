from statistics import mean


def average(function):

    def inner(*args):
        function(*args)
        print('Средне арифметическое чисел', args, '=', mean(args))

    return inner


@average
def sum_of_numbers(*args):
    print('Сумма чисел', args, '=', sum(args))
    return args


sum_of_numbers(2, 3, 3, 4)
