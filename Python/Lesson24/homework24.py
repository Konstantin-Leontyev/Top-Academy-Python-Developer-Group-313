class Car:

    def __init__(
            self,
            model,
            year_of_issue,
            manufacturer,
            engine_power,
            color,
            price,
    ):
        self.model = model
        self.year_of_issue = year_of_issue
        self.manufacturer = manufacturer
        self.engine_power = engine_power
        self.color = color
        self.price = price

    def __str__(self):
        header = 'Персональные данные '.center(40, '*')
        body = f'\nНазвание модели: {self.model}\n'\
               f'Год выпуска: {self.year_of_issue}\n'\
               f'Производитель: {self.manufacturer}\n'\
               f'Мощность двигателя: {self.engine_power} л.с.\n'\
               f'Цвет машины: {self.color}\n'\
               f'Цена: {self.price}\n'
        footer = "=" * 40
        return header + body + footer

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def set_year_of_issue(self, year_of_issue):
        self.year_of_issue = year_of_issue

    def get_year_of_issue(self):
        return self.year_of_issue

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def get_manufacturer(self):
        return self.manufacturer

    def set_engine_power(self, engine_power):
        self.engine_power = engine_power

    def get_engine_power(self):
        return self.engine_power

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price


if __name__ == '__main__':
    car = Car(
        model='X7 M50i',
        year_of_issue='2021',
        manufacturer='BMW',
        engine_power=530,
        color='white',
        price=10790000
    )

    print(car)
