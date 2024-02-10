# class Point(object):
#     x = 1
#     y = 1
#
#
# point = Point()


# class Human():
#     name = 'name'
#     birthday = '00.00.0000'
#     phone = '00-00-00'
#     country = 'country'
#     city = 'city'
#     address = 'street, house'
#
#     def print_info(self):
#         print('Персональные данные '.center(40, '*'))
#         print(f'Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона : {self.phone}\n'
#               f'Страна: {self.country}\nГород: {self.city}\nДомашний адрес: {self.address}')
#         print('=' * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_address(self, address):
#         self.address = address
#
#     def get_address(self):
#         return self.address
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info('Юля', '23.05.1986', '45-46-98', 'Россия', 'Москва', 'Чистопрудный бульвар, 1A')
# h1.print_info()
# h1.set_address('ул. Ленина, 56')
# h1.print_info()
# h1.set_name('Юлия')
# print(h1.get_name())

class Person:
    skill = 10
    # name = ''
    # surname = ''
    count = 0

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        print('Инициализатор класса', self)
        # self.count += 1
        Person.count += 1

    def __del__(self):
        print('Удаление экземпляра', self)

    def print_info(self, name, surname):
        # self.name = name
        # self.surname = surname
        print('Данные сотрудника:', self.name, self.surname)

    def add_skill(self, skill):
        self.skill += skill
        print('Квалификация сотрудника:', self.skill)


# p1 = Person()
# p1.print_info('Виктор', 'Резник')
p1 = Person('Виктор', 'Резник')
# p1.print_info()
# p1.add_skill(3)
print(p1.count)

# p2 = Person()
# p2.print_info('Анна', 'Долгих')
p2 = Person('Анна', 'Долгих')
# p2.print_info()
# p2.add_skill(5)
print(p2.count)