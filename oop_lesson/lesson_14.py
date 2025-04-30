# __add__() - сложение (можно использовать __radd__() если объект идет справа)
# или __iadd__() если нужно присвоить результат +=
# такая штука есть у дандер методов связанных с арифметическими операциями
# просто добавляем r или i

# __sub__() - вычитание
# __mul__() - умножение
# __truediv__() - деление
# __floordiv__() - целочисленное деление
# __mod__() - остаток от деления
# __pow__() - возведение в степень




class Clock: 
    __DAY = 86400 # число секунд в сутках

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("The seconds must be an integer!!!")
        # остаток от деления работает таким образом, что если мы 
        # вторым параметром передаем большее число он возвращает 
        # значение первого параметра
        self.seconds = seconds % self.__DAY

    def get_item(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"seconds = {self.seconds},\ntime = {h:02}:{m:02}:{s:02}"
    
    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("The other must be an integer or Clock!!!")
        
        sc = other.seconds if isinstance(other, Clock) else other
        return self.__class__(self.seconds + sc)
    
    # по сути после такой записи у нас выполняется self.__add__(other)
    def __radd__(self, other):
        return self + other
    
    def __iadd__(self, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("The other must be an integer or Clock!!!")
        
        # не создаем новый объект, а просто увеличиваем секунды в старом
        sc = other.seconds if isinstance(other, Clock) else other
        self.seconds += sc
        return self


c1 = Clock(1000)
# благодаря __add__ можно складывать объекты
c1 = c1 + 2000
print(c1.get_item())


c2 = Clock(3000)
c2 = c1 + c2
print(c2.get_item())


c3 = Clock(4000)
c4 = c1 + c2 + c3
print(c4.get_item())


# благодаря __radd__ можно складывать объекты справа
c4 = 100 + c3
print(c4.get_item())

c4 += 200
print(c4.get_item())