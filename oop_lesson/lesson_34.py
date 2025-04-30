# классы это тоже обьекты, но их создает метакласс

# метакласс - это тоже обьект но его уже нельзя создать

# если type передать не один аргумент а 3 (имя, список родительских классов, словарь с атрибутами), то он создаст новый класс

# обычный класс
class  Point:
    MIN_COORD = 0
    MAX_COORD = 100 


# создание с помощью метакласса
A = type("Point", (), {'MIN_COORD': 0, 'MAX_COORD': 100})

pt = A()
print(pt.MIN_COORD)


class B1:
    pass 

class C1:
    pass


# новый класс который наследуется от B1 и C1
N = type('Point', (B1, C1), {'MIN_COORD': 100, 'MAX_COORD': 200})
print(N.__mro__)

def method1(self):
    print(self.__dict__)

N = type('Point', (B1, C1), {'MIN_COORD': 100, 'method1': method1})
N.method1(N())

N = type('Point', (B1, C1), {'MIN_COORD': 100, 'method1': lambda self: print(self.__dict__)})
N.method1(N())