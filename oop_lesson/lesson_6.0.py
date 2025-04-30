# ИНКАПСУЛЯЦИЯ

# attribute - public (без двух или одного  подчеркивания) атрибуты имеют публичный режим  доступа (public)

# _attribute - protected (с одним подчеркиванием) атрибуты имеют защищенный режим доступа (protected)
# и служат для обращения внутри класса и во всех его дочерних классах 
# лишь предостерегает программиста от изменения этого атрибута напрямую (но явно не ограничивает)

# __attribute - private (с двумя подчеркиваниями) атрибуты имеют приватный режим доступа (private)
# и служат только для обращения внутри класса
# ограничивает программиста от обращения к этому атрибуту из вне, но внутри класса можно использовать и изменять этот атрибут 

class Point:
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__validate(x) and self.__validate(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Недопустимые значения координат')

    # приватный метод для валидации данных (сделаем методом класса, тк вдруг он будет обращаться к каким-то дополнительным атрибутам класса)
    @classmethod
    def __validate(cls, x):
        # проверка типа переменной на тип данных int или float
        return type(x) in (int, float)

    # Метода ниже являются интерфейсными методами (сеттер и геттер)
    # Эти методы крайне важны, так как класс стоит воспринимать как единое целое, и что бы случайно не 
    # нарушить целостность работы алгоритма то следует взаимодействовать с ним только через публичные методы 
    # Пример машина: управляй через руль, если залезешь чинить шины особенно во время работы тобипизда
    # Сеттер и Геттер так же нужны для валидации данных перед их присвоением
    def set_coords(self, x, y):
        if self.__validate(x) and self.__validate(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Недопустимые значения координат')

    def get_coords(self):
        return self.__x, self.__y

pt = Point(1, 2)
print(pt.get_coords())
pt.set_coords(3, 2)
print(pt.get_coords())
print(pt.__dict__) # видим {'_Point__x': 3, '_Point__y': 2} Кодовое имя имен экземпляра класса
# делать так очень не рекомендуется, но фактически можно получить доступ к приватному атрибуту
print(pt._Point__x) 




# Создайте класс BankAccount:
# Добавьте приватные атрибуты __balance (баланс счета) и __pin (пин-код).
# Инициализируйте их в конструкторе (__init__), где баланс по умолчанию равен 0, а пин-код задается при создании объекта.
# Добавьте приватный метод __validate_pin, который будет проверять, совпадает ли переданный пин-код с пин-кодом счета.

# Ответ:
# class BankAccount:
#     def __init__(self, pin):
#         self.__balance = 0
#         self.__pin = pin

#     def __validate_pin(self, pin):
#         return self.__pin == pin


# Добавьте методы для управления балансом:
# Создайте метод deposit, который будет принимать сумму и пин-код. Если пин-код верный, увеличивайте баланс на указанную сумму.
# Создайте метод withdraw, который будет принимать сумму и пин-код. Если пин-код верный и на счету достаточно средств, уменьшайте баланс на указанную сумму.
# Создайте метод get_balance, который будет возвращать текущий баланс, если пин-код верный.

# Ответ:
# class BankAccount:
#     def __init__(self, pin):
#         self.__balance = 0
#         self.__pin = pin

#     def __validate_pin(self, pin):
#         return self.__pin == pin

#     def deposit(self, amount, pin):
#         if self.__validate_pin(pin):
#             self.__balance += amount
#         else:
#             raise ValueError("Неверный пин-код")

#     def withdraw(self, amount, pin):
#         if self.__validate_pin(pin):
#             if self.__balance >= amount:
#                 self.__balance -= amount
#             else:
#                 raise ValueError("Недостаточно средств")
#         else:
#             raise ValueError("Неверный пин-код")

#     def get_balance(self, pin):
#         if self.__validate_pin(pin):
#             return self.__balance
#         else:
#             raise ValueError("Неверный пин-код")

# Проверьте работу класса:
# Создайте объект BankAccount с пин-кодом 1234.
# Пополните счет на 1000 и выведите баланс.
# Попробуйте снять 500 и выведите баланс.
# Попробуйте снять 600 (должно вызвать ошибку, так как недостаточно средств).

# Ответ:
# account = BankAccount(1234)
# account.deposit(1000, 1234)
# print(account.get_balance(1234))  # Вывод: 1000
# account.withdraw(500, 1234)
# print(account.get_balance(1234))  # Вывод: 500
# try:
#     account.withdraw(600, 1234)
# except ValueError as e:
#     print(e)  # Вывод: Недостаточно средств



# Создайте класс Calculator:
# Добавьте защищенный (protected) метод __validate, который будет проверять, что переданное значение является числом (тип int или float).
# Добавьте метод add, который будет принимать два числа, проверять их с помощью _validate и возвращать их сумму.

# Ответ:
# class Calculator:
#     def _validate(self, value):
#         return isinstance(value, (int, float))

#     def add(self, a, b):
#         if self._validate(a) and self._validate(b):
#             return a + b
#         else:
#             raise ValueError("Оба аргумента должны быть числами")

# Проверьте работу класса:
# Создайте объект Calculator.
# Попробуйте сложить два числа и выведите результат.
# Попробуйте сложить число и строку. Что происходит?

# Ответ:
# calc = Calculator()
# print(calc.add(5, 3))  # Вывод: 8
# try:
#     print(calc.add(5, "abc"))  # Ошибка: ValueError
# except ValueError as e:
#     print(e)  # Вывод: Оба аргумента должны быть числами