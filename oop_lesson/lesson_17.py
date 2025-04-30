class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print('Вызов метода __len__')
        # квадрат длины радиус вектора
        return self.x * self.x + self.y * self.y
    
    def __bool__(self):
        # bool должен обязательно возвращать True или False
        print('Вызов метода __bool__')
        return self.x == self.y

p = Point(0, 0)
print(len(p))

# так же магический метод __len__ переопределяет и функцию bool  
# пока маг метод __bool__ не определен в классе 
print(bool(p)) 
# теперь False будет только при отсутствующих координатах (0,0)

# __bool__ обычно явно не вызывается 
# а срабатывает например в условных операторах 

if p: 
    print('объект p дает True')
else:
    print('объект p дает False')


