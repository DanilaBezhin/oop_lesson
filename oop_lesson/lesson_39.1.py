# еще один способ объявления dataclass (функция make_dataclass)
from dataclasses import make_dataclass, field

# обычный класс 
class Car:
    def  __init__(self, model, max_speed, price):
        self.model = model
        self.max_speed = max_speed
        self.price = price
    
    def get_max_speed(self):
        return self.max_speed


# Параметр namespace в функции make_dataclass позволяет расширять функциональность создаваемого класса, 
# добавляя собственные методы или атрибуты. Это полезно для динамического создания классов с кастомной логикой, 
# не ограничиваясь только полями, описанными через dataclass

CarData = make_dataclass('CarData', [('model', str),
                                    'max_speed',
                                    ('price', float, field(default=0.0))],
                        namespace={'get_max_speed': lambda self: self.max_speed})


c = CarData('Audi', 250, 1000.0)
print(c.get_max_speed())
print(c)