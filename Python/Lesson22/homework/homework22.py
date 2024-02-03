FILE_NAME = 'text.txt'


def creat_file():
    with open(FILE_NAME, 'w') as data:
        # file.write('"Замена строки в текстовом файле";\n'
        #            'изменить строку в списке;\n'
        #            'записать список в файл;\n'
        #            )
        data.write('Строка № 1;\n'
                   'Строка № 2;\n'
                   'Строка № 3;\n'
                   'Строка № 4;\n'
                   'Строка № 5;\n'
                   'Строка № 6;\n'
                   )


def input_index(message: str, data_list: list[str]) -> int:
    index = int(input(message))
    if index not in range(1, len(data_list) + 1) or index < 1:
        print('Убедитесь что введен корректный номер строки и повторите попытку.')
        return input_index(message, data_list)
    else:
        return index


if __name__ == '__main__':

    creat_file()

    with open(FILE_NAME, 'r') as file:
        string_list = file.readlines()
        # print(string_list)
        string_1 = input_index('Введите номер первой строки: ', string_list)
        string_2 = input_index('Введите номер второй строки: ', string_list)

        (string_list[string_1 - 1],
         string_list[string_2 - 1]) = (f'Строка № {string_1} была заменена на строку № {string_2};\n',
                                       f'Строка № {string_2} была заменена на строку № {string_1};\n')
        # print(string_list)

    with open(FILE_NAME, 'w') as file:
        file.writelines(string_list)
