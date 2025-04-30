# Декораторы: 
# @classmethod - метод класса
# @staticmethod - статический метод

class Vector:
    # атрибуты класса 
    MIN_COORD = 0
    MAX_COORD = 100

    # Метод класса для валидации входных данных. Работает с атрибутами класса, 
    # но не может обращаться к локальным атрибутам экземпляра
    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    # При создании объекта значениям атрибутов устанавливаем 0 (по умолчанию) а далее проверяем 
    # на валидность с помощью метода класса validate. Ссылка на метод получаем путем обращения к self тк
    # self так же хранит информацию о классе (в данном случае Vector)  
    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y
        
        # Можем вызывать статический метод из методов внутри класса
        print(self.norm2(3, 2))

    # Как и в методе __init__ мы можем обратится к локальным атрибутам экземпляра а так же к атрибутам класса
    def get_coords(self):
        return self.x, self.y
    
    # с помощью @staticmethod декоратора мы можем определять статические методы, 
    # которые не имеют доступа ни к атрибуту класса ни к атрибутам экземпляра
    # своеобразная независимая функция (в атрибутах нет self и cls)
    @staticmethod
    def norm2(x, y):
        # Можем обратится и к атрибутам класса через Vector.MAX_COORD
        # НО!!! НЕ РЕКОМЕНДУЕТСЯ тк при смене названия класса, упадет
        # Рекомендуется - использовать только независимые значения
        return x**2 + y**2
    
v = Vector(-10, 20)
res = Vector.get_coords(v) #ИЛИ v.get_coords()
print(res)

print(Vector.validate(40))

print(Vector.norm2(3, 2))



# Создайте класс Circle:
# Добавьте атрибуты класса: PI = 3.14159 и DEFAULT_RADIUS = 1.
# Реализуйте метод класса from_diameter, который будет принимать диаметр и возвращать новый экземпляр класса Circle с радиусом, вычисленным из диаметра.

# Ответ:
# class Circle:
#     PI = 3.14159
#     DEFAULT_RADIUS = 1

#     def __init__(self, radius):
#         self.radius = radius

#     @classmethod
#     def from_diameter(cls, diameter):
#         radius = diameter / 2
#         return cls(radius)

# Создайте экземпляр класса Circle с использованием метода from_diameter:
# Создайте объект с диаметром 10 и выведите его радиус.

# Ответ:
# circle = Circle.from_diameter(10)
# print(circle.radius)  # Вывод: 5.0


# Добавьте метод класса validate_radius, который будет проверять, что радиус находится в допустимом диапазоне (например, от 1 до 100):
# Используйте этот метод в __init__, чтобы установить радиус по умолчанию, если переданный радиус невалиден.

# Ответ:
# class Circle:
#     PI = 3.14159
#     DEFAULT_RADIUS = 1
#     MIN_RADIUS = 1
#     MAX_RADIUS = 100

#     def __init__(self, radius):
#         if not self.validate_radius(radius):
#             self.radius = self.DEFAULT_RADIUS
#         else:
#             self.radius = radius

#     @classmethod
#     def validate_radius(cls, radius):
#         return cls.MIN_RADIUS <= radius <= cls.MAX_RADIUS

#     @classmethod
#     def from_diameter(cls, diameter):
#         radius = diameter / 2
#         return cls(radius)

# Проверьте работу валидации:
# Создайте объект с радиусом 150 и убедитесь, что радиус был установлен по умолчанию.

# Ответ:
# circle = Circle(150)
# print(circle.radius)  # Вывод: 1 (по умолчанию)




# Создайте класс MathOperations:
# Добавьте статический метод add, который будет принимать два числа и возвращать их сумму.
# Добавьте статический метод multiply, который будет принимать два числа и возвращать их произведение.

# Ответ:
# class MathOperations:
#     @staticmethod
#     def add(a, b):
#         return a + b

#     @staticmethod
#     def multiply(a, b):
#         return a * b

# Используйте статические методы:
# Вызовите методы add и multiply для чисел 5 и 3 и выведите результаты.

# Ответ:
# print(MathOperations.add(5, 3))        # Вывод: 8
# print(MathOperations.multiply(5, 3))    # Вывод: 15

# Добавьте статический метод is_even, который будет проверять, является ли число четным:
# Используйте этот метод для проверки числа 10.

# Ответ:
# class MathOperations:
#     @staticmethod
#     def add(a, b):
#         return a + b

#     @staticmethod
#     def multiply(a, b):
#         return a * b

#     @staticmethod
#     def is_even(number):
#         return number % 2 == 0

# print(MathOperations.is_even(10))  # Вывод: True


# Создайте класс Rectangle и добавьте статический метод is_square:
# Метод должен принимать длину и ширину прямоугольника и возвращать True, если это квадрат, и False в противном случае.

# Ответ:
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     @staticmethod
#     def is_square(length, width):
#         return length == width

# rect = Rectangle(5, 5)
# print(Rectangle.is_square(rect.length, rect.width))  # Вывод: True



# Создайте класс Temperature:
# Добавьте атрибуты класса: MIN_TEMP = -273.15 (минимальная температура по Цельсию) и MAX_TEMP = 1000.
# Добавьте метод класса validate_temp, который будет проверять, что температура находится в допустимом диапазоне.
# Добавьте статический метод celsius_to_fahrenheit, который будет конвертировать температуру из Цельсия в Фаренгейт.

# Ответ:
# class Temperature:
#     MIN_TEMP = -273.15
#     MAX_TEMP = 1000

#     def __init__(self, celsius):
#         if not self.validate_temp(celsius):
#             raise ValueError("Температура вне допустимого диапазона")
#         self.celsius = celsius

#     @classmethod
#     def validate_temp(cls, celsius):
#         return cls.MIN_TEMP <= celsius <= cls.MAX_TEMP

#     @staticmethod
#     def celsius_to_fahrenheit(celsius):
#         return celsius * 9/5 + 32

# Создайте экземпляр класса Temperature и проверьте конвертацию:
# Создайте объект с температурой 25 градусов Цельсия и выведите его значение в Фаренгейтах.

# Ответ:
# temp = Temperature(25)
# print(Temperature.celsius_to_fahrenheit(temp.celsius))  # Вывод: 77.0

# Проверьте валидацию температуры:
# Попробуйте создать объект с температурой -300 градусов Цельсия и убедитесь, что выбрасывается исключение.

# Ответ:
# try:
#     temp = Temperature(-300)
# except ValueError as e:
#     print(e)  # Вывод: Температура вне допустимого диапазона