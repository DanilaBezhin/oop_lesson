class Animal:
    def sound(self):
        print("The animal makes a sound")

class Dog(Animal):
    name = "Пэс"

# У класса animals много дандер методов, хотя м ыне прописывали не одного, дело в том что все базовые классы не явно наследуются
# от object класса, в котором все это реализовано. В дочерних же классах, наследование идет от базового класса а в базовом уже от
# object.
print(Animal.__dict__)

d = Dog()

# Как узнать является ли другой класс, подклассом другого класса?
# функция issubclass
print(issubclass(Dog, Animal))

# важный момент работает она только с классами
# print(issubclass(d, Dog)) # Ошибка TypeError: issubclass() arg 1 must be a class

print(issubclass(Dog, object)) # True

# для проверки обьектов на то являются ли они экземплярами класса исполльзуем isinstanse
# но isinstans может работать и с классами 
print(isinstance(d, Dog)) # True
print(isinstance(d, Animal)) # True
print(isinstance(d, object)) # True


# важный момент 
# все стандартные типы данных являются классами 
# int str dict list set tuple 

print(issubclass(tuple, object)) # True

# так как они являются классами, нам ничего не мешает наследоваться от них

class Vector(list):
    # переопределили строковое представление списка
    def __str__(self):
        return " ^_^ ".join([str(i) for i in self])


v = Vector([1, 2, 3])
print(v)

v.append(4)
print(v)









# Задание: Создайте класс CaseInsensitiveString, 
# который игнорирует регистр букв при сравнении строк.
class CaseInsensitiveString(str):
    def __eq__(self, other):
        return self.lower() == other.lower()

# Пример использования:
s1 = CaseInsensitiveString("Hello")
s2 = CaseInsensitiveString("hello")
s3 = CaseInsensitiveString("HeLLO")
print(s1 == s2)  # Вывод: True
print(s2 == s3)  # Вывод: True


# Задание: Создайте класс PasswordString, который скрывает содержимое строки при выводе.
class PasswordString(str):
    def __str__(self):
        return "*" * len(self)

# Пример использования:
ps = PasswordString("secret")
print(ps)  # Вывод: ******

