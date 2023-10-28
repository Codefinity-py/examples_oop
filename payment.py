# Розглянемо систему обробки платежів. Давайте створимо класи для реалізації цієї системи.
# Створіть абстрактний клас "Платіж" (абстракція) з атрибутами "сума" і "дата". Цей клас буде містити загальну інформацію про кожен платіж.
# Створіть два підкласи "КредитнийПлатіж" і "ДебетовийПлатіж", які успадковують від класу "Платіж" (успадкування).
# У кожному з цих підкласів визначте метод "обробити", який буде виводити інформацію про платіж.
# Використовуйте інкапсуляцію, щоб зробити атрибут "сума" приватним, і надайте методи для доступу до цього атрибуту.
# Створіть список об'єктів "Платіж" (поліморфізм), включаючи як "Кредитні платежі", так і "Дебетові платежі", і викличте метод "обробити" для кожного об'єкта.

from abc import ABC, abstractmethod


class Payment(ABC):
    def __init__(self, amount, date):
        self.__amount = amount
        self.date = date

    def get_amount(self):
        return self.__amount

    @abstractmethod
    def process(self):
        pass


class CreditPayment(Payment):
    def process(self):
        print(f"Кредитний платіж на суму {self.get_amount()} гривень оброблено і датовано {self.date}")


class DebitPayment(Payment):
    def process(self):
        print(f"Дебетовий платіж на суму {self.get_amount()} гривень оброблено і датовано {self.date}")


payment_1 = CreditPayment(1000, '20-10-2023')
payment_2 = DebitPayment(1500, '27-02-2022')

payments = {payment_1, payment_2}

for payment in payments:
    payment.process()
