class Point2D: 
    # накладывает ограничения только  на атрибуты объекта, а не класса
    __slots__ = ("x", "y", "__length")

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__length = f"{(x * x + y * y) ** 0.5:.2f}"

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value


p =  Point2D(3, 1)
print(p.length)
p.length = 5
print(p.length)


class Point3D(Point2D):
    # если написать __slots__ и тут, будет  доступны все  атрибуты и отсюда и от базового класса 
    pass


# можем использовать все те же методы, а так же  игнорировать ограничение __slots__ тк оно не наследуется 
p1 = Point3D(3, 1)
print(p1.length)
p1.length = 5
print(p1.length)
p1.z = 10
print(p1.z)
# свойства x и y есть но в dict они не попадают 
print(p1.x, p1.y)
print(p1.__dict__)