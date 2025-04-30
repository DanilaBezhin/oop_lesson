# Пользовательские метакласыы

# class Point:
#     MAX_COORD = 100
#     MIN_COORD = 0


# def create_class(name, base, attrs):
#     attrs.update({'MAX_COORD': 100, 'MIN_COORD': 0})
#     return type(name, base, attrs)


# class Point(metaclass=create_class):
#     def get_coords(self):
#         return (0, 0)


# pt = Point()
# print(pt.__dict__)
# print(pt.MAX_COORD)
# print(pt.get_coords())




# ======================================


class Meta(type):
    def __new__(cls, name, base, attrs):
        attrs.update({'MAX_COORD': 100, 'MIN_COORD': 0})
        return type.__new__(cls, name, base, attrs)


class Point(metaclass=Meta):
    def get_coords(self):
        return (0, 0)


pt = Point()
pt.MAX_COORD 
pt.get_coords()
