# магические методы сравнения

# Операнд - аргумент операции;
# __eq__ для равенства ==
# __ne__ для неравенства !=
# __lt__ для меньше <
# __le__ для меньше или равно <=
# __gt__ для больше >
# __ge__ для больше или равно >=


class Clock:
    __DAY: int = 86400  # количество секунд в сутках

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Seconds must be an integer.")
        
        # Сохраняем секунды в пределах одного дня
        self.seconds: int = seconds % self.__DAY

    @classmethod
    def __verify_data(cls, value) -> bool:
        if not isinstance(value, (int, Clock)):
            raise TypeError("Can only compare to other clocks.")
        
        return value.seconds if isinstance(value, Clock) else value
         
    def __eq__(self, value) -> bool:
        sc = self.__verify_data(value)
        return self.seconds == sc
    
    def __lt__(self, value) -> bool:
        sc = self.__verify_data(value)
        return self.seconds < sc

c1 = Clock(1100)
c2 = Clock(1000)

# по умолчанию сравниваются адреса экземпляров (id)
# после изменения метода __eq__ мы сравниваем секунды 
print(f"c1 == c2: {c1 == c2}") 

# после реализации метода __eq__ будет работать корректно тк если 
# не прописан dunder метод __ne__ то будет вызван метод __eq__
# так как под капотом с1 != с2 обрабатывается как not(c1 == c2) 
print(f"c1 != c2: {c1 != c2}")

# а операторы <, <=, >, >= вообще вызывают ошибку без использования __lt__
print(f"c1 < c2: {c1 < c2}")
print(f"c1 > c2: {c2 < c1}")
# при реализации __lt__ можно использовать и > тк пайтон сделаем подмену 
# с1 > c2 -> c2 < c1 (работает как и в случае с __eq__ только тогда когда 
# метод противоположный (в данном случае __gt__) явно не определен)


# так же это будет работать и с методами __le__ и __ge__