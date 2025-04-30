# пример наследования

class Vehicle:
    def __init__(self, wheels, capacity):
        self.wheels = wheels
        self.capacity = capacity

    @property
    def wheels(self):
        return self._wheels

    @wheels.setter
    def wheels(self, wheels):
        if not isinstance(wheels, int) or wheels <= 0:
            raise ValueError("Количество колес должно быть целым положительным числом!")
        self._wheels = wheels

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Вместимость должна быть целым положительным числом!")
        self._capacity = capacity

    def describe(self):
        return f"Транспортное средство с {self.wheels} колесами, вместимостью {self.capacity} человек."


class Car(Vehicle):
    def __init__(self, wheels, capacity, doors):
        super().__init__(wheels, capacity)
        self.doors = doors

    @property
    def doors(self):
        return self._doors

    @doors.setter
    def doors(self, doors):
        if not isinstance(doors, int) or doors <= 0:
            raise ValueError("Количество дверей должно быть целым положительным числом!")
        self._doors = doors


class Bicycle(Vehicle):
    def __init__(self, wheels, capacity, has_basket):
        super().__init__(wheels, capacity)
        self.has_basket = has_basket  # Используем свойство has_basket

    @property
    def has_basket(self):
        return self._has_basket

    @has_basket.setter
    def has_basket(self, has_basket):
        if not isinstance(has_basket, bool):
            raise ValueError("Значение для корзины должно быть булевым (True или False).")
        self._has_basket = has_basket

try:
    car = Car(4, 5, 4)
    print(car.describe())
    car.doors = 2  # Изменяем количество дверей через свойство
    print(f"Обновленный автомобиль: {car.describe()}")

    bicycle = Bicycle(2, 1, True)
    print(bicycle.describe())
    bicycle.has_basket = False  # Изменяем наличие корзины через свойство
    print(f"Обновленный велосипед: {bicycle.describe()}")

    # Пример ошибки: присвоение неверного значения
    car.wheels = -1
except ValueError as e:
    print(e)