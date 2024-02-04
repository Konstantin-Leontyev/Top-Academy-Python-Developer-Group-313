"""
Скрипт сгенерирует необходимые каталоги и фалы. Часть файлов заполнить строками их путей.
Отобразит схему содержимого созданного каталога. С указанием директорий, файлов и их размера.
"""
import os


directories = ['Work/F1/', 'Work/F2/F21',]
for directory in directories:
    os.makedirs(directory)

files_dict = {
    'Work': ['w.txt',],
    'Work/F1': ['f11.txt', 'f12.txt', 'f13.txt',],
    'Work/F2/F21': ['f211.txt', 'f212.txt',],
}

base_names = ['w.txt', 'f12.txt', 'f211.txt', 'f212.txt']

for folder, filenames in files_dict.items():
    for filename in filenames:
        path = os.path.join(folder, filename)
        with open(path, 'w') as file:
            if os.path.basename(path) in base_names:
                file.write(path)


def print_info(directory):
    """Выводит структуру вложенных директорий и файлов."""
    print(directory)
    for root, dirs, files in os.walk(directory):
        count = root.count(os.sep)
        separator = '\t' * count
        for file in files:
            print(f'{separator}|\n{separator}-- {os.path.basename(file)} - file - {os.path.getsize(os.path.join(root, file))} bytes')
        for _dir in dirs:
            print(f'{separator}|\n{separator}-- {os.path.basename(_dir)} - dir')


print_info('Work')
