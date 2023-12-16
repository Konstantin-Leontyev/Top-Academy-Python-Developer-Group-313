
VOWELS = {'а', 'е', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'ё'}

string = input('Введите строку: ')

# count = 0
# for letter in string:
#     if letter.lower() in VOWELS:
#         count += 1
#
# print('Количество гласных равно:', count)

tmp_list = [letter for letter in string if letter.lower() in VOWELS]

print('Количество гласных равно:', len(tmp_list))


