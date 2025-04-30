class Vector3D:
    def __init__(self, x: int, y: int, z: int, custom_length: int):
        self.x = x
        self.y = y
        self.z = z
        self.length = round((x * x + y * y + z * z) ** 0.5, 2)
        self.custom_length = round(((x * x + y * y + z * z) ** 0.5)) ** custom_length


v1 = Vector3D(3, 4, 5, 3)
print(v1.__dict__)


# пример этого класса через дата класс
from dataclasses import dataclass, field, InitVar


@dataclass
class V3D:
    # исключение из repr преставления
    x: int = field(repr=False)
    y: int
    # исключение из сравнения
    z: int = field(compare=False)
    # length: float = round((x * x + y * y + z * z) ** 0.5, 2) # NameError: name 'x' is not defined
    # ->
    # init=False - исключение из инициализации
    length: float = field(init=False, compare=False)
    custom_l: InitVar[bool] = True

    # метод который вызывается после инициализации обьекта датаклассом 
    def __post_init__(self, custom_l: bool):
        if custom_l:
            self.length = round((self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5, 2)
        else:
            self.length = round((self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5)
        


v1 = V3D(13, 14, 15, False)
# когда датакласс формирует repr он формирует его с явно прописными атрибутами в данном случа x y z
# а length формируется на лету, что бы выйти из этой ситуации нужно прописать этот атрибут -> 
print(v1) # V3D(x=3, y=4, z=5) # -> после добавления field(init=False) legth не будет добавлен в init а сформируется после
print(v1.__dict__) # {'x': 3, 'y': 4, 'z': 5, 'length': 7.07}

