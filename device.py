# Розглянемо абстракцію електронного пристрою, такого як смартфон.
# Створіть клас "Пристрій" (абстракція) з атрибутом "назва". Цей клас буде представляти загальні характеристики електронних пристроїв.
# Створіть підклас "Смартфон", який успадковується від класу "Пристрій" (успадкування). Додайте атрибути, такі як "операційна система" і "розмір екрану".
# Використовуйте інкапсуляцію, щоб приховати атрибут "назва" і надайте метод для доступу до нього.
# Створіть метод "запустити_додаток" для класу "Смартфон", який приймає назву додатка і виводить повідомлення про запуск цього додатка.
# Створіть кілька об'єктів класу "Смартфон" і викличте метод "запустити_додаток" для кожного об'єкта (поліморфізм).

from abc import ABC


class Device(ABC):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Smartphone(Device):

    def __init__(self, name, os, screen_size):
        super().__init__(name)
        self.os = os
        self.screen_size = screen_size

    def start_application(self, application):
        print(application, f'run success on {self.get_name()}')


device = Smartphone('samsung', 'android', 6.2)
device.start_application('browser')
