# Как гибко работать с приватными свойствами в Python?
# Прошлый пример можно переписать в более правильный вид так:
# через property
class Person: 
    def __init__(self, name, age):
        # приватные атрибуты
        self.__name = name
        self.__age = age

    # декоратор property (обязательно перед getter)
    # теперь getter будет объектом свойства приватного свойства age 
    @property
    def age(self):
        return self.__age
    
    # декоратор сеттер, через age тк, age теперь объект свойства
    # + что бы все работало, нужно использовать одинаковые имена методов
    @age.setter
    def age(self, age):
        self.__age = age

    # вызывается при удалении свойства
    @age.deleter
    def age(self):
        del self.__age


p = Person('John', 30)
p.age = 31
print(p.age, p.__dict__)
del p.age
print(p.__dict__)
