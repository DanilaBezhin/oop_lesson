class Student: 
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __getitem__(self, item):
        if 0 <= item <= len(self.marks) - 1:
            return self.marks[item]

        raise IndexError("Оценка с таким индексом не существует!")
    
    def __setitem__(self, key, value):
        # обычно мы можем писать отрицательный индекс, но в данном случае мы так решили
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен быть целым числом!")
        
        # данный способ позволяет добавлять элементы сверх конца списка игнорируя ошибку IndexError: list assignment index out of range
        # пропущенные строки заполняются None, что бы это работало нужно поставить [] что бы получить именно список а не none type
        if key > len(self.marks) - 1:
            off = key - (len(self.marks) - 1)
            self.marks.extend([None] * off)

        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен быть целым числом!")
        
        del self.marks[key]

s1 = Student("John", [2, 2])
# таким образом мы можем получить доступ к элементу списка (оценок) по индексу
print(s1.marks[1])

# если мы захотим получать оценки в формате 
# print(s1[1]) то получим ошибку TypeError: 'Student' object is not subscriptable
# но мы можем поправить этот момент реализовав магический метод __getitem__ 
print(s1[0])


# что бы изменять элемент списка мы можем использовать dunder метод __setitem__
s1[3] = 5
print(s1.marks)

s1[10] = 4
print(s1.marks)


# __delitem__ вызывается при удалении элемента списка объекта Student
del s1[1]
print(s1.marks)



# Выжимка по уроку:
# Магические методы для работы с индексами:

# __getitem__ — позволяет обращаться к элементу объекта как к списку (например, obj[1]).
# __setitem__ — позволяет изменять элемент по индексу (например, obj[2] = 5).
# __delitem__ — позволяет удалять элемент по индексу (например, del obj[0]).

# Особенности:
# Можно добавлять элементы за пределами текущего размера списка (автоматическое расширение с None).
# Проверка типов и значений индекса (например, запрет отрицательных индексов).
# Пример использования:

s1 = Student("John", [2, 2])
print(s1[0])      # 2
s1[3] = 5         # [2, 2, None, 5]
del s1[1]         # [2, None, 5]




# Задание: Напиши свой класс BookShelf
# Цель: Закрепить работу с магическими методами __getitem__, __setitem__, __delitem__.

# Шаги:
# Создай класс BookShelf, который хранит список книг (в виде строк).

# Реализуй __init__, принимающий список книг (по умолчанию пустой).

# Реализуй __getitem__, чтобы можно было получить книгу по индексу:
# shelf = BookShelf(["Harry Potter", "Lord of the Rings"])
# print(shelf[0])  # "Harry Potter"

# Реализуй __setitem__, чтобы можно было изменять книгу по индексу или добавлять новые (расширять список, как в примере с Student):
# shelf[2] = "The Hobbit"  # ["Harry Potter", "Lord of the Rings", "The Hobbit"]

# Реализуй __delitem__, чтобы можно было удалять книгу по индексу:
# del shelf[0]  # ["Lord of the Rings", "The Hobbit"]