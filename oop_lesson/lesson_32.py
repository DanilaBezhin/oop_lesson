import copy

class DefinedVector:
    def __init__(self, vector):
        self.__vector = vector 

    def __enter__(self):
        self.__temp = copy.deepcopy(self.__vector)
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__vector[:] = self.__temp


v1 = [1, 1, 1]
v2 = [1, 2, 2]

try:
    with DefinedVector(v1) as dv:
        for i, v in enumerate(dv):
            dv[i] += v2[i]
except Exception as e:
    print(e)

print(v1)
