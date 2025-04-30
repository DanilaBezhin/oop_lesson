# # Пример разработки класса Person
# # с полями ФИ, возраст, серия и номер паспорта вес

# # модуль re обеспечивает операции сопоставления регулярных выражений
# import re

# class Person:
#     def __init__(self, first_name, last_name, age, passport, weight):
#         # оставим проверку имени, так как ее изменение в этой реализации не предусмотренно 
#         self.verify_name(first_name, last_name)

#         # такие проверки тут больше не нужны, так как мы исправили приватные атрибуты 
#         # на обычную запись self.__attr -> self.attr, что позволило сразу вызвать сеттеры 
#         # self.verify_age(age)
#         # self.verify_passport(passport)
#         # self.verify_weight(weight)

#         self.__first_name = first_name
#         self.__last_name = last_name
#         self.age = age
#         self.passport = passport
#         self.weight = weight

#     @staticmethod
#     def verify_name(first_name, last_name):
#         # Регулярное выражение для проверки имени и фамилии
#         pattern = r'^[a-zA-Zа-яА-Я]+$'

#         if type(first_name) != str or type(last_name) != str:
#             raise TypeError('The first and last name must be strings!!!')
        
#         if len(first_name) == 0 or len(last_name) == 0:
#             raise ValueError('The first and last name cannot be empty!!!')

#         # Проверка на соответствие регулярному выражению с помощью re.match
#         if not bool(re.match(pattern, first_name)) or not bool(re.match(pattern, last_name)):
#             raise ValueError('The first and last name must consist only of Cyrillic or Latin letters!!!')

#     @staticmethod
#     def verify_age(age):
#         if type(age) != int or age < 14 or age > 100:
#             raise TypeError('The age must be an integer from 14 to 100!!!')

#     @staticmethod
#     def verify_weight(weight):
#         if type(weight) != float or weight < 20 or weight > 500:
#             raise TypeError('The weight must be a float from 20 to 500!!!')
        
#     @staticmethod
#     def verify_passport(passport):
#         if type(passport) != str:
#             raise TypeError('The passport must be a string!!!')
        
#         proc_pa = passport.split()
#         if len(proc_pa) != 2 or len(proc_pa[0]) != 4 or len(proc_pa[1]) != 6:    
#             raise ValueError('Incorrect passport format!!!')
        
#         if not proc_pa[0].isdigit() or not proc_pa[1].isdigit():
#             raise ValueError('The passport number must consist only of digits!!') 

#     @property
#     def fl_name(self):
#         return f"{self.__first_name} {self.__last_name}"   

#     @property
#     def age(self):
#         return self.__age

#     @age.setter
#     def age(self, age):
#         self.verify_age(age)
#         self.__age = age

#     @property
#     def weight(self):
#         return self.__weight
    
#     @weight.setter
#     def weight(self, weight):
#         self.verify_weight(weight)
#         self.__weight = weight

#     @property
#     def passport(self):
#         return self.__passport
    
#     @passport.setter
#     def passport(self, passport):
#         self.verify_passport(passport)
#         self.__passport = passport

# p1 = Person('Ivan', 'Ivanov', 25, '1233 123233', 80.2)
# p1.age = 39
# p1.weight = 89.0

# print(p1.fl_name)
# print(p1.age)
# print(p1.__dict__)


class Person:
    def __init__(self, name: str, age: int, gender: str):
        self._name = name  # Приватное свойство для имени
        self._age = age    # Приватное свойство для возраста
        self._gender = gender  # Приватное свойство для пола

    @property
    def name(self) -> str:
        """Геттер для имени."""
        return self._name

    @name.setter
    def name(self, value: str):
        """Сеттер для имени."""
        if not isinstance(value, str):
            raise ValueError("Имя должно быть строкой")
        self._name = value

    @property
    def age(self) -> int:
        """Геттер для возраста."""
        return self._age

    @age.setter
    def age(self, value: int):
        """Сеттер для возраста."""
        if not isinstance(value, int) or value < 0:
            raise ValueError("Возраст должен быть положительным целым числом")
        self._age = value

    @property
    def gender(self) -> str:
        """Геттер для пола."""
        return self._gender

    @gender.setter
    def gender(self, value: str):
        """Сеттер для пола."""
        if value not in ["male", "female", "other"]:
            raise ValueError("Пол должен быть 'male', 'female' или 'other'")
        self._gender = value

    @staticmethod
    def is_adult(age: int) -> bool:
        """Статический метод для проверки, является ли человек взрослым."""
        return age >= 18


# Пример использования
person = Person(name="Иван", age=25, gender="male")

print(person.age)  # Вывод: Person(name=Иван, age=25, gender=male)
print(person.name)  # Вывод: Person(name=Иван, age=25, gender=male)
print(person.gender)  # Вывод: Person(name=Иван, age=25, gender=male)

# Использование сеттеров
person.name = "Алексей"
person.age = 30
person.gender = "other"

print(person.age)  # Вывод: Person(name=Иван, age=25, gender=male)
print(person.name)  # Вывод: Person(name=Иван, age=25, gender=male)
print(person.gender)  # Вывод: Person(name=Иван, age=25, gender=male)

# Использование статического метода
print(Person.is_adult(person.age))  # Вывод: True