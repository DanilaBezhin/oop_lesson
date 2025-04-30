# Дескрипторы в Python — это мощный инструмент, который позволяет вам контролировать доступ к атрибутам объектов. 
# Они используются для создания объектов, которые могут управлять тем, как другие объекты взаимодействуют с их атрибутами.


# Дескриптор — это просто класс, который реализует один или несколько из следующих методов:
# __get__(self, instance, owner): Этот метод вызывается, когда вы пытаетесь получить доступ к атрибуту.
# __set__(self, instance, value): Этот метод вызывается, когда вы пытаетесь установить значение атрибута.
# __delete__(self, instance): Этот метод вызывается, когда вы пытаетесь удалить атрибут.


# Простой пример дескриптора
# Допустим, у нас есть класс Temperature, который хранит температуру в градусах Цельсия, но мы хотим, 
# чтобы температура всегда была в положительном значении. Мы можем создать дескриптор для этого.
class PositiveNumber:
    def __get__(self, instance, owner):
        return instance._temperature

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Temperature can't be negative")
        instance._temperature = value

    def __delete__(self, instance):
        del instance._temperature

class Temperature:
    temperature = PositiveNumber()

    def __init__(self, temperature):
        self.temperature = temperature

# Пример использования
t = Temperature(25)
print(t.temperature)  # Выведет: 25

t.temperature = 10
print(t.temperature)  # Выведет: 10

t.temperature = -5  # Ошибка: ValueError: Temperature can't be negative



# Заключение
# Дескрипторы — это мощный механизм в Python, который позволяет контролировать доступ к атрибутам объектов. 
# Они могут быть полезны, когда вам нужно добавить логику в процесс чтения, записи или удаления атрибутов класса.