# Как гибко работать с приватными свойствами в Python?
# через property
class Person: 
    def __init__(self, name, age):
        # приватные атрибуты
        self.__name = name
        self.__age = age

    # геттер
    def get_age(self):
        return self.__age
    
    # сеттер
    def set_age(self, age):
        self.__age = age

    # объект property с геттером и сеттером, автоматически выполняет геттер при считывании данных 
    # и сеттер при записи. Это работает, поскольку age имеет больший приоритет
    age = property(get_age, set_age)


p = Person('John', 30)
# даже так, age не изменит приватное свойство, а при дальнейшем обращении
# к p.age будет вызываться property, тк приоритет этого атрибута выше
p.__dict__['age'] = 33

p.age = 31
print(p.age, p.__dict__)

