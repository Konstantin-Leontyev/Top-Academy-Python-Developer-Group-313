tpl = tuple(input('Введите по порядку, без пробелов, элементы кортежа: '))
# tmp = 253523651
lst = []
print(tpl)
for num in tpl:
    if num not in lst:
        lst.append(num)
        print(f'Количеств {num} = {tpl.count(num)}')
