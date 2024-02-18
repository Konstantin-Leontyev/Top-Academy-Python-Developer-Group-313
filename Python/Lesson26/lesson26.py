class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('.'))
        date1 = cls(day, month, year)  # date1 = Date(23, 10 2024)
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        if date_as_string.count('.') == 2:
            day, month, year = map(int, date_as_string.split('.'))
            return day <= 31 and month <= 12 and year <= 2100

    def string_to_db(self):
        return f'{self.year}-{self.month}-{self.day}'


# string_date = '23.10.2024'
# # day, month, year = map(int, string_date.split('.'))
# # print(day, month, year) # 23 10 2024
# date = Date(day, month, year)
# print(date.string_to_db())

# date2 = Date.from_string('23.10.2024')  # date2 = Date(23, 10, 2024)
# print(date2.string_to_db())
# date3 = Date.from_string('25.12.2023')
# print(date3.string_to_db())

# dates = [
#     '30.12.2023',
#     '30-12-2020',
#     '01.01.2024',
#     '12.31.2020',
# ]
#
# for string_date in dates:
#     if Date.is_date_valid(string_date):
#         date = Date.from_string(string_date)
#         print(date.string_to_db())
#     else:
#         print('Неправильная дата или формат строки с датой')


# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     SUFFIX_RUB = 'RUB'
#     SUFFIX_USD = 'USD'
#     SUFFIX_EUR = 'EUR'
#
#     def __init__(self, surname, num, percent, value=0):
#         self.surname = surname
#         self.num = num
#         self.percent = percent
#         self.value = value
#         print(f'Счёт №{self.num} принадлежащий {self.surname} был открыт.')
#         print('*' * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счёт №{self.num} принадлежащий {self.surname} был закрыт.')
#
#     @classmethod
#     def set_rate_usd(cls, new_rate):
#         cls.rate_usd = new_rate
#
#     @classmethod
#     def set_rate_eur(cls, new_rate):
#         cls.rate_eur = new_rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def convert_to_usd(self):
#         usd_value = self.convert(self.value, self.rate_usd)
#         print(f'Состояние счёта: {usd_value} {Account.SUFFIX_USD}')
#
#     def convert_to_eur(self):
#         eur_value = self.convert(self.value, self.rate_eur)
#         print(f'Состояние счёта: {eur_value} {Account.SUFFIX_EUR}')
#
#     def print_balance(self):
#         print(f'Текущий баланс: {self.value} {Account.SUFFIX_RUB}.')
#
#     def edit_owner(self, new_surname):
#         self.surname = new_surname
#
#     def add_percent(self):
#         self.value += self.value * self.percent
#         print(f'Проценты были успешно начислены!')
#         self.print_balance()
#
#     def withdraw_money(self, amount):
#         if amount > self.value:
#             print(f'К сожалению у вас нет {amount} {Account.SUFFIX_RUB}')
#         else:
#             self.value -= amount
#             print(f'{amount} {Account.SUFFIX_RUB} было успешно снято!')
#         self.print_balance()
#
#     def add_money(self, amount):
#         self.value += amount
#         print(f'{amount} {Account.SUFFIX_RUB} успешно добавлено!')
#         self.print_balance()
#
#     def print_info(self):
#         print('Информация о счете:')
#         print('-' * 20)
#         print(f'№{self.num}')
#         print(f'Владелец: {self.surname}')
#         self.print_balance()
#         print(f'Проценты: {self.percent:.0%}')
#         print('-' * 20)
#
#
#
#
# acc = Account('Долгих', '12345', 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# Account.set_rate_usd(2)
# Account.set_rate_eur(3)
# print()
# acc.convert_to_usd()
# acc.convert_to_eur()
# acc.edit_owner('Дюма')
# acc.print_info()
# print()
# acc.add_percent()
# print()
# acc.withdraw_money(100)
# print()
# acc.withdraw_money(3000)
# print()
# acc.add_money(5000)
# print()
# acc.withdraw_money(3000)
# print()

import re


class UserData:
    def __init__(self, fio, old, ps, weight):
        # self.verify_fio(fio)
        # self.verify_old(old)
        # self.verify_ps(ps)
        # self.verify_weight(weight)

        #self.__fio = fio
        self.fio = fio
        # self.__old = old
        self.old = old
        # self.__password = ps
        self.ps = ps
        # self.__weight = 0
        self.weight = weight

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, new_fio):
        self.verify_fio(new_fio)
        self.__fio = new_fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, new_old):
        self.verify_old(new_old)
        self.__old = new_old

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        self.verify_ps(new_password)
        self.__password = new_password

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, new_weight):
        self.verify_weight(new_weight)
        self.__weight = new_weight


    @staticmethod
    def verify_fio(fio):
        if not isinstance(fio, str):
            raise TypeError('ФИО должно быть строкой')
        if re.findall(r'[^a-zа-яё\s-]', fio, re.IGNORECASE):
            raise ValueError('Использованы не допустимые символы')
        f = fio.split()
        if len(f) != 3:
            raise TypeError('Неверный формат ФИО')

    @staticmethod
    def verify_old(old):
        if not isinstance(old, int) or not 14 < old < 120:
            raise TypeError('Возраст должен быть числом в диапазоне от 14 до 120')

    @staticmethod
    def verify_weight(w):
        if not isinstance(w, float) or w < 20:
            raise TypeError('вес должен быть вещественным числом от 20 кг и выше')

    @staticmethod
    def verify_ps(ps):
        if not isinstance(ps, str):
            raise TypeError('Паспорт должен быть строкой')
        s = ps.split()
        if (len(s) != 2
                or len(s[0]) != 4
                or len(s[1]) != 6
            ):
            raise TypeError('Не верный формат серии и номера паспорта')
        for p in s:
            if not p.isdigit():
                raise TypeError('Серия и номер паспорта должны быть числами')


p1 = UserData('Волков Игорь Николаевич', 26, '1234 567890', 80.8)
print(p1.fio)
print(p1.old)
print(p1.ps)
print(p1.weight)
