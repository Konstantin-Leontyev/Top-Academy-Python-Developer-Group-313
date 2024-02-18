import re


class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    SUFFIX_RUB = 'RUB'
    SUFFIX_USD = 'USD'
    SUFFIX_EUR = 'EUR'

    def __init__(self, surname, num, percent, value=0):
        self.surname = self.set_surname(surname)
        self.num = num
        self.percent = percent
        self.value = value
        print(f'Счёт №{self.num} принадлежащий {self.surname} был открыт.')
        print('*' * 50)

    def __del__(self):
        print('*' * 50)
        print(f'Счёт №{self.num} принадлежащий {self.surname} был закрыт.')

    @classmethod
    def set_rate_usd(cls, new_rate):
        cls.rate_usd = new_rate

    @classmethod
    def set_rate_eur(cls, new_rate):
        cls.rate_eur = new_rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, (int | float)):
            raise TypeError('Убедитесь что введено цифровое значение для баланса')
        if new_value < 0:
            raise ValueError('Отрицательное значение баланса не допустимо.')
        self.__value = round(float(new_value), 2)

    def get_surname(self):
        return self.surname

    def set_surname(self, new_surname: str):
        if not isinstance(new_surname, str):
            raise TypeError('Фамилия должна быть строкой')
        elif re.findall(r'[^а-яё-]', new_surname, re.IGNORECASE):
            raise ValueError('Допустимы только буквы А-я и -')
        self.surname = new_surname

    def add_money(self, amount):
        self.value += amount
        print(f'{amount} {Account.SUFFIX_RUB} успешно добавлено!')
        self.print_balance()

    def convert_to_usd(self):
        usd_value = self.convert(self.value, self.rate_usd)
        print(f'Состояние счёта: {usd_value} {Account.SUFFIX_USD}')

    def convert_to_eur(self):
        eur_value = self.convert(self.value, self.rate_eur)
        print(f'Состояние счёта: {eur_value} {Account.SUFFIX_EUR}')

    def add_percent(self):
        self.value += self.value * self.percent
        print(f'Проценты были успешно начислены!')
        self.print_balance()

    def withdraw_money(self, amount):
        if amount > self.value:
            print(f'К сожалению у вас нет {amount} {Account.SUFFIX_RUB}')
        else:
            self.value -= amount
            print(f'{amount} {Account.SUFFIX_RUB} было успешно снято!')
        self.print_balance()

    def print_balance(self):
        print(f'Текущий баланс: {self.value} {Account.SUFFIX_RUB}.')

    def print_info(self):
        print('Информация о счете:')
        print('-' * 20)
        print(f'№{self.num}')
        print(f'Владелец: {self.surname}')
        self.print_balance()
        print(f'Проценты: {self.percent:.0%}')
        print('-' * 20)


if __name__ == '__main__':
    acc = Account('Долгих', '12345', 0.03, 5000)
    acc.print_info()
    acc.convert_to_usd()
    acc.convert_to_eur()
    Account.set_rate_usd(2)
    Account.set_rate_eur(3)
    print()
    acc.convert_to_usd()
    acc.convert_to_eur()
    acc.set_surname('Дюма')
    acc.print_info()
    print()
    acc.add_percent()
    print()
    acc.withdraw_money(100)
    print()
    acc.withdraw_money(3000)
    print()
    acc.add_money(5000)
    print()
    acc.withdraw_money(3000)
    print()