class Person:

    def __init__(self, name: str, age: int):
        __name = ''
        __age = 0
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError('Имя задается строкой')
        self.__name = new_name

    @name.deleter
    def name(self):
        del self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if not isinstance(new_age, int):
            raise TypeError('Возраст задаётся цифрами')
        self.__age = new_age

    @age.deleter
    def age(self):
        del self.__age


person = Person(name='Irina', age=26)
print(person.__dict__)
person.name = 'Igor'
person.age = 31
print(person.__dict__)
del person.name
print(person.__dict__)
