# Завдання: Створіть клас "Студент" з атрибутами (змінними) "ім'я", "вік" і "середній бал".
# Потім створіть кілька об'єктів цього класу, заповніть їх даними та виведіть інформацію про кожного студента.

class Student:
    def __init__(self, name, age, average_rate):
        self.name = name
        self.age = age
        self.average_rate = average_rate

    def display_info(self):
        print(f"Імʼя студента: {self.name}")
        print(f"Вік студента: {self.age}")
        print(f"Середня оцінка студента: {self.average_rate}\n")


student1 = Student("Максим", 19, 4.8)
student2 = Student("Вадим", 20, 4.4)
student3 = Student("Данііл", 30, 3.9)

print("Інформація про студентів:")
student1.display_info()
student2.display_info()
student3.display_info()
