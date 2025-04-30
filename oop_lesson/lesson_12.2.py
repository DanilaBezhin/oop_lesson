# Эта программа вычисляет численную производную функции
# sin(x) в заданной точке, используя декоратор Derivate
import math


class Derivate:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x)) / dx
    

@Derivate
def df_sin(x):
    return math.sin(x)


print(df_sin(math.pi / 2))