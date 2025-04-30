# Наследование в объектно-ориентированном программировании (ООП) на Python — это механизм, 
# позволяющий одному классу (называемому дочерним или производным) унаследовать свойства и методы другого класса 
# (называемого родительским или базовым).

# Зачем нужно наследование?
# Основная идея наследования — повторное использование кода. Когда у вас есть класс с определенными функциями, 
# и вы хотите создать новый класс, который будет иметь такие же функции, но с небольшими изменениями или дополнениями, 
# вместо того чтобы переписывать весь код, вы можете унаследовать этот класс и добавить только новые или измененные части.

# Родительский элемент 
class Geom:
    name = 'Geom'

    def set_coords(self, x, y):
        self.x = x
        self.y = y

# Дочерний элемент
class Line(Geom):
    # overriding переопределение 
    name = 'Line'

    def draw(self):
        print('draw line')

# Дочерний элемент
class Rect(Geom):
    def draw(self):
        print('draw rect')


l = Line()
l.set_coords(3, 3)
l.draw()

r = Rect()
r.set_coords(5, 5)
r.draw()

print(l.__dict__, r.__dict__)

# сначала метод или атрибут ищется в текущем классе, если его нет, то идет к родительскому классу и ищет уже там, 
# self, при вызове метода базового класса, является ссылкой на объект класса, который вызывает метод 




#! Выжимка по уроку с важными моментами:

# Наследование — это механизм в ООП, позволяющий одному классу (дочернему) унаследовать свойства и методы другого класса (родительского). Это помогает избежать дублирования кода и упрощает его повторное использование.

# Родительский класс — это базовый класс, который предоставляет свои методы и атрибуты для наследования.
# Дочерний класс — это производный класс, который может использовать методы и атрибуты родительского класса, а также добавлять или переопределять их.

# Переопределение (overriding) — это процесс изменения поведения метода или значения атрибута родительского класса в дочернем классе. При этом метод или атрибут с тем же именем в дочернем классе заменяет родительский.

# Поиск атрибутов и методов происходит следующим образом:
# Сначала Python ищет атрибут или метод в текущем классе.
# Если не находит, он обращается к родительскому классу.
# self всегда является ссылкой на объект, вызвавший метод, независимо от того, где находится метод (в текущем или родительском классе).



# Задание на закрепление
# Создайте базовый класс Vehicle (транспортное средство), который будет содержать общие свойства 
# и методы для всех видов транспорта. Затем создайте два дочерних класса: Car (автомобиль) и 
# Bike (велосипед), которые будут расширять функциональность базового класса.

# Требования:

# Базовый класс Vehicle:
    # Атрибуты:
        # name (название транспортного средства, например, "Автомобиль" или "Велосипед").
        # speed (текущая скорость, по умолчанию 0).

    # Добавить атрибут класса year of manufacture (год выпуска)

    # Методы:
        # accelerate(value) — увеличивает скорость на указанное значение.
        # decelerate(value) — уменьшает скорость на указанное значение (но не ниже 0).
        # info() — выводит информацию о транспортном средстве (название и текущую скорость).

# Дочерний класс Car:
    # Переопределите атрибут year of manufacture на 2095
    # Добавьте новый метод honk() — выводит "Би-би!".

# Дочерний класс Bike:
    # Переопределите атрибут year of manufacture на 2007
    # Добавьте новый метод ring_bell() — выводит "Динь-динь!".

# Тестирование:
    # Создайте объекты Car и Bike.
    # Увеличьте и уменьшите их скорость с помощью методов accelerate и decelerate.
    # Выведите информацию о каждом транспортном средстве с помощью метода info.
    # Протестируйте специфические методы (honk для автомобиля и ring_bell для велосипеда).



# Базовый класс
class Vehicle:
    def __init__(self, name="Транспортное средство"):
        self.name = name
        self.speed = 0

    def accelerate(self, value):
        self.speed += value
        print(f"{self.name} ускоряется до {self.speed} км/ч.")

    def decelerate(self, value):
        self.speed = max(0, self.speed - value)
        print(f"{self.name} снижает скорость до {self.speed} км/ч.")

    def info(self):
        print(f"{self.name}: текущая скорость {self.speed} км/ч.")

# Дочерний класс Car
class Car(Vehicle):
    def __init__(self):
        super().__init__(name="Автомобиль")

    def honk(self):
        print("Би-би!")


# Дочерний класс Bike
class Bike(Vehicle):
    def __init__(self):
        super().__init__(name="Велосипед")

    def ring_bell(self):
        print("Динь-динь!")


# Тестирование
car = Car()
bike = Bike()

# Ускорение и замедление
car.accelerate(50)
car.decelerate(20)
car.info()

bike.accelerate(10)
bike.decelerate(5)
bike.info()

# Специфические методы
car.honk()
bike.ring_bell()


import random

def play_game():
    deck = list(range(1, 12))  
    random.shuffle(deck)      
    
    scores = [0, 0]           
    current_player = 1        
    stop_flags = [False, False]  
    
    while True:
        print(f"\n=== Player {current_player}'s Turn ===")
        print(f"Player {current_player}'s current score: {scores[current_player - 1]}")
        
        if stop_flags[current_player - 1]: 
            print(f"Player {current_player} has already decided to stop.")
        else:
            choice = input("Draw a card? (yes/no): ").lower()
            
            if choice == "no":
                print(f"Player {current_player} decided to stop drawing cards.")
                stop_flags[current_player - 1] = True 
                
                if all(stop_flags):
                    print("\nBoth players decided to stop. Ending the game...")
                    break
        
        if not stop_flags[current_player - 1]:
            card = deck.pop(0)   
            scores[current_player - 1] += card  
            
            print(f"Player {current_player} drew a card with value {card}. Their new score is: {scores[current_player - 1]}")
            
            if scores[current_player - 1] > 20:  
                print(f"Player {current_player} lost because their score exceeded 20!")
                return f"Player {3 - current_player} wins!"
        
        current_player = 2 if current_player == 1 else 1
    
    print("\n=== Final Results ===")
    print(f"Player 1's score: {scores[0]}")
    print(f"Player 2's score: {scores[1]}")
    
    if abs(20 - scores[0]) < abs(20 - scores[1]):
        return "Player 1 wins!"
    elif abs(20 - scores[0]) > abs(20 - scores[1]):
        return "Player 2 wins!"
    else:
        return "It's a tie!"

print(play_game())