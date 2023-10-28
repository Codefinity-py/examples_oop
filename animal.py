# Створіть базовий клас "Тварина" з атрибутами "ім'я" і "вік". Потім створіть підкласи "Собака" і "Кішка",
# додайте їм методи "голос" для видачі звуку, який є характерним для кожної тварини.
# Створіть об'єкти собаки і кішки і дозвольте їм видавати звуки. Додатково, додайте атрибут "порода" для кожного підкласу
# і метод для його визначення.

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def voice(self):
        pass


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def voice(self):
        print("Bark")


class Cat(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def voice(self):
        print("Meow")


dog = Dog("Рекс", 2, "Овчарка")
cat = Cat("Барсик", 1.5, "Персидський")
dog.voice()
cat.voice()
