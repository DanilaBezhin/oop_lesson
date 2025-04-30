# __str__() - для отображения информации об объекте класса для пользователей, например в print или str 

# __repr__() - для отображения информации об объекте класса для разработчиков, например в режиме отладки

# __len__() - позволяет применять функцию len к экземпляру класса

# __abs__() - позволяет применять функцию abs к экземпляру класса


# реализация __str__ и __len__
class Car: 
    def __init__(self, name, speed):
        self.name = name 
        self.speed = speed

    # __class__ - возвращает имя текущего класса
    def __repr__(self):
        return f"{self.__class__}: {self.name}"
    
    def __str__(self):
        return self.name
    
car1 = Car("Lada", 120)
print(str(car1))
print(car1)


# реализация __abs__ и __len__
class Point:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)
    
    def __abs__(self):
        return list(map(abs, self.__coords))
    


# теперь можно применять len и abs
p = Point(1, -2, 3)
print(len(p)) # 3
print(abs(p)) # [1, 2, 3]