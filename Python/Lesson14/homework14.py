from typing import Union


def fill_data() -> list:
    """Заполняет базу данных студентов"""
    global students_count
    # Ввод пользователем количества студентов.
    students_count = int(input('Количество студентов: '))
    # Заполнение базы студентов.
    data: list[dict[str: Union[str, int]]] = [
        {
            'id': i,
            'Имя': input(f'Имя {i}-го студента: '),
            'Фамилия': input(f'Фамилия {i}-го студента: '),
            'Балл': int(input('Балл: '))
        } for i in range(1, students_count + 1)
    ]

    return data


def get_average_grade(data: list[dict[str: Union[str, int]]]) -> Union[int, float]:
    """Функция подсчета среднего бала студентов."""
    grades: list[int] = [student['Балл'] for student in data]
    return round(sum(grades) / students_count)


def print_report(data: list[dict[str: Union[str, int]]]):
    """Функция вывода на печать запроса к базе данных."""
    average_grade: Union[int, float] = get_average_grade(data)
    print(f'Средний бал: {average_grade}. Студентов с балом выше среднего:')
    for student in data:
        if student['Балл'] > average_grade:
            print(student['Имя'])


if __name__ == '__main__':
    # Авто тест.
    # Глобальная переменная для хранения количества студентов.
    students_count: int = 5
    students: list[dict[str: Union[str, int]]] = [
        {'id': 1, 'Имя': 'Игорь', 'Фамилия': 'Исаев', 'Балл': 12},
        {'id': 2, 'Имя': 'Валентин', 'Фамилия': 'Киреев', 'Балл': 7},
        {'id': 3, 'Имя': 'Виктор', 'Фамилия': 'Степанов', 'Балл': 4},
        {'id': 4, 'Имя': 'Григорий', 'Фамилия': 'Иванов', 'Балл': 9},
        {'id': 5, 'Имя': 'Дмитрий', 'Фамилия': 'Кузнецов', 'Балл': 6}
    ]

    # Для ручного заполнения.
    # # Глобальная переменная для хранения количества студентов.
    # students_count: int
    # students = fill_data()

    print_report(students)
