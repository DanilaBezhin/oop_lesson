from dataclasses import dataclass, field, InitVar
from typing import Any


class GoodsMethodsFactory:
    @staticmethod
    def gat_init_measure() -> list:
        return [0, 0, 0]



@dataclass
class Goods:
    # без анатации атрибут будет содержаться в классе, но будет пропущен декоратором data class 
    current_uid = 0

    uid: int = field(init=False)
    price: Any = None 
    weight: Any = None


    def __post_init__(self):
        print(" Goods post init")
        Goods.current_uid += 1
        self.uid = Goods.current_uid

@dataclass
class Book(Goods):
    title: str = ""
    author: str = ""
    price: float = 0.0
    weight: int | float = 0.0
    sheet_weight: InitVar[int | float] = 1.2
    # то, что вернет метод то и будет значением по умолчанию (пример реализации своей функции)
    measure: list = field(default_factory=GoodsMethodsFactory.gat_init_measure)


    # сначала метод post init ищется в дочернем классе, если находится выполняется именно он 
    def __post_init__(self, sheet_weight):
        self.measure = [sheet_weight/1000, sheet_weight/100, sheet_weight]
        print("Book post init")
        # что бы вызвать метод post init в родительском классе нужно использовать super()
        # для обычный init такого делать не нужно (при использовании dataclass, а без нужно)
        super().__post_init__()



# после такой реализации init book будет таким: 
# def __init__(self, uid: Any, price: float = 0.0, weight: int | float = 0.0, title: str = "", author: str = ""):

b = Book(1000, 100, "Python OOP", "Балакирев С.М.")
print(b)

b1 = Book()
print(b1)