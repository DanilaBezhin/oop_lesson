# Декоратор @abstractmethod и класс ABC (от Abstract Base Class) используются в Python для создания абстрактных классов и 
# абстрактных методов, которые помогают обеспечить обязательность реализации определенных методов в дочерних классах.


# Зачем нужны @abstractmethod и ABC
# @abstractmethod:

# Этот декоратор используется для обозначения метода как абстрактного. Абстрактный метод — это метод, 
# который объявляется в абстрактном классе, но не имеет реализации.

# Дочерние классы, которые наследуются от абстрактного класса, обязаны реализовать все его абстрактные методы. 
# Если дочерний класс не реализует все абстрактные методы, он сам становится абстрактным и его нельзя инстанцировать.


# ABC:

# ABC — это специальный базовый класс, от которого наследуются абстрактные классы. 
# Если класс наследуется от ABC, это означает, что он может содержать абстрактные методы.

# ABC используется для создания абстрактных базовых классов, которые могут служить основой для других классов, 
# требуя от них реализации определенных методов.


from abc import ABC, abstractmethod

# Создаем абстрактный класс
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass  # Абстрактный метод не имеет реализации

    @abstractmethod
    def perimeter(self):
        pass  # Абстрактный метод не имеет реализации

# Дочерний класс, который реализует абстрактные методы
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Дочерний класс, который реализует абстрактные методы
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius


c = Circle(5)
print(c.area())
print(c.perimeter())


r = Rectangle(10, 5)
print(r.area())
print(r.perimeter())

# Создайте абстрактный класс Vehicle, который будет содержать следующие абстрактные методы:
# start_engine(), который будет отвечать за запуск двигателя.
# stop_engine(), который будет отвечать за остановку двигателя.
# move(), который будет описывать движение транспортного средства.
# Затем реализуйте два дочерних класса: Car и Bicycle.

# Класс Car должен реализовывать все три метода, и его метод move должен выводить, что машина едет.
# Класс Bicycle должен также реализовывать все три метода, и его метод move должен выводить, что велосипед едет.

from abc import ABC, abstractmethod

# Создаем абстрактный класс Vehicle
class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def move(self):
        pass

# Дочерний класс Car
class Car(Vehicle):
    def start_engine(self):
        print("Двигатель машины запущен.")

    def stop_engine(self):
        print("Двигатель машины остановлен.")

    def move(self):
        print("Машина едет.")

# Дочерний класс Bicycle
class Bicycle(Vehicle):
    def start_engine(self):
        print("У велосипеда нет двигателя.")

    def stop_engine(self):
        print("Велосипед остановлен.")

    def move(self):
        print("Велосипед едет.")

# Примеры использования
car = Car()
car.start_engine()
car.move()
car.stop_engine()

print()  # Печатаем пустую строку для разделения вывода

bicycle = Bicycle()
bicycle.start_engine()
bicycle.move()
bicycle.stop_engine()