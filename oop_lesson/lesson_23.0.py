# Особенности формирования приватных атрибутов при наследовании
# приватные атрибуты жестко привязываются к классу, внутри которого создаются 
# защищенный атрибут с одним подчеркиванием, не сможет так жестко блокировать обращение к атрибуту, но лучше не обращаться 
# к там атрибутом из вне тк, они создаются для внутренних алгоритмов класса 

class Geom:
    __name = 'Geom'

    def __init__(self, x, y):
        print(f'Geom: __init__ for {self.__class__}')
        self.__x = x
        self.__y = y
        self._name = self.__name
        # при вызове  этого конструктора в других классах наследуемых от Geom свойства  будут записаны как '_Geom__x': 1, '_Geom__y': 2

    # из-за особенности формирования приватных атрибутов при наследовании данную функцию нельзя поместить в классе Rect
    def get_coords(self):
        return (self.__x, self.__y)

    @staticmethod
    def _verify(coord):
        return 0  <= coord <= 100


class Rect(Geom):
    name = 'Rect'

    def __init__(self, x, y, fill):
        print(f'Rect: __init__')
        super().__init__(x, y)
        self._verify(x)
        self.__fill = fill
        # а эти свойства  в  свою очередь будут записаны, как '_Rect__w': 3, '_Rect__h': 4
        

r = Rect(1, 2, 'RED')
# поскольку у атрибутов 
print(r.get_coords())
print(r.__dict__)




#* protected
# class Parent: 
#     def __init__(self):
#         self._protected = 'protected prop'

# class Child(Parent):
#     def access_protected(self):
#         return self._protected
    
# ch = Child()
# print(ch.access_protected())
# print(ch._protected)

# *private
# class Parent: 
#     def __init__(self):
#         self.__private = 'private prop'

# class Child(Parent):
#     def access_private(self):
#         try:
#             return self.__private 
#         except AttributeError as e:
#             return str(e)
    
# ch1 = Child()
# ch2 = Parent()
# print(ch1.__dict__)
# print(ch1.access_private())




# Создайте класс Employee (сотрудник), который будет иметь следующие характеристики:

# Защищенный атрибут _name — имя сотрудника.
# Приватный атрибут __salary — зарплата сотрудника.
# Метод get_salary, который возвращает текущую зарплату.
# Метод set_salary, который позволяет установить новую зарплату, но только если она больше текущей.
# Создайте дочерний класс Manager, который наследует Employee. Добавьте в него:

# Защищенный атрибут _bonus — бонус для менеджера.
# Метод add_bonus, который увеличивает зарплату на значение бонуса.


class Employee:
    def __init__(self, name, salary):
        self._name = name  # Защищенный атрибут
        self.__salary = salary  # Приватный атрибут

    def get_salary(self):
        return self.__salary  # Возвращаем приватный атрибут

    def set_salary(self, new_salary):
        if new_salary > self.__salary:
            self.__salary = new_salary
            print(f"Зарплата обновлена: {self.__salary}")
        else:
            print("Новая зарплата должна быть больше текущей")

    def __str__(self):
        return f"Сотрудник: {self._name}, Зарплата: {self.__salary}"


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)  # Наследуем атрибуты родительского класса
        self._bonus = bonus  # Защищенный атрибут

    def add_bonus(self):
        self.set_salary(self.get_salary() + self._bonus)
        print(f"Бонус добавлен. Новая зарплата: {self.get_salary()}")

    def __str__(self):
        return f"Менеджер: {self._name}, Зарплата: {self.get_salary()}, Бонус: {self._bonus}"


# Создаем объекты
employee = Employee("Иван", 50000)
print(employee)  # Вывод: Сотрудник: Иван, Зарплата: 50000

employee.set_salary(60000)  # Вывод: Зарплата обновлена: 60000
print(employee)  # Вывод: Сотрудник: Иван, Зарплата: 60000

manager = Manager("Анна", 80000, 10000)
print(manager)  # Вывод: Менеджер: Анна, Зарплата: 80000, Бонус: 10000

manager.add_bonus()  # Вывод: Бонус добавлен. Новая зарплата: 90000
print(manager)  # Вывод: Менеджер: Анна, Зарплата: 90000, Бонус: 10000