class Point:
    # Класс как область видимости:
    # переменные нижи являются атрибутами класса, в экземплярах их нет, но мы можем обратится к ним через ссылку self или cls
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    # ОШИБКА тк, MIN_COORD это атрибут класса а не экземпляра
    # при такой записи создаться новый атрибут для экземпляра
    # а атрибут класса не изменится!!!
    # def set_min_coords(self, x):
    #     self.MIN_COORD = x

    # Автоматически вызывается при получении свойства класса с именем item
    # (при ОБРАЩЕНИИ к атрибутам экземпляра класса)
    # Один из примеров: создание запрета на обращение например к 'x'
    def __getattribute__(self, item):
        print(f"Вызов метода __getattribute__ {self} {item}")
        if item != 'x':
            return object.__getattribute__(self, item)
        else: 
            raise AttributeError("Доступ к атрибуту 'x' запрещен!")

    # Автоматически вызывается при присвоении атрибута экземпляру класса  
    # self - экземпляр, key - имя атрибута, value - значение которое присваиваем
    # Для примера запретим добавление атрибутов НЕ с именем 'x' и 'y'
    def  __setattr__(self, key, value):
        print(f"Вызов метода __setattr__ {self} {key} {value}")
        if key == 'x' or key == 'y':
            object.__setattr__(self, key, value)
        else:
            raise AttributeError(f"Доступ к атрибуту '{value}' запрещен!")
        

    # Автоматически вызывается при обращении к несуществующему атрибуту
    # Хоть класса, хоть экземпляра
    # Для примера механика, которая исключает ошибки к несуществующему свойству
    # экземпляра класса, и возвращает False
    def __getattr__(self, item):
        return False

    # Автоматически вызывается при удалении атрибута экземпляра
    def __delattr__(self, item):
        print(f"Вызов метода __delattr__ {self} {item}")
        # само удаление атрибута
        object.__delattr__(self, item)
    
pt1 = Point(1, 2)
pt2 = Point(3, 4)
print(pt1.yy)
print(pt2.y)
del pt1.y



# Задание: Создание класса Library
# Создайте класс Library, который будет управлять коллекцией книг. Каждая книга имеет название, автора и год издания. Класс должен предоставлять методы для добавления, удаления и поиска книг.

# Требования:
# Метод __init__:
# Инициализирует объект библиотеки.
# Принимает необязательный аргумент books (список книг, где каждая книга — это словарь с ключами title, author, year).
# Если books не передан, создает пустой список книг.


# Приватный метод __validate_book:
# Принимает книгу (словарь) и проверяет, что она содержит все необходимые ключи (title, author, year).
# Если книга невалидна, выбрасывает исключение ValueError.


# Дандер-метод __setattr__:
# Переопределите метод __setattr__, чтобы запретить прямое добавление атрибутов, кроме books.
# Если пользователь пытается добавить атрибут, отличный от books, выбрасывайте исключение AttributeError.


# Метод add_book:
# Принимает книгу (словарь) и добавляет её в библиотеку.
# Использует приватный метод __validate_book для проверки книги перед добавлением.


# Метод remove_book:
# Принимает название книги и удаляет её из библиотеки.
# Если книга не найдена, выбрасывает исключение ValueError.

# Метод find_books_by_author:
# Принимает имя автора и возвращает список всех книг этого автора.



class Library:
    def __init__(self, books=None):
        if books is None:
            self.books = []
        else:
            self.books = books

    def __validate_book(self, book):
        if not all(key in book for key in ['title', 'author', 'year']):
            raise ValueError("Книга должна содержать ключи: title, author, year")

    def __setattr__(self, name, value):
        if name != 'books':
            raise AttributeError(f"Невозможно добавить атрибут {name}")
        super().__setattr__(name, value)

    def add_book(self, book):
        self.__validate_book(book)
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book['title'] == title:
                self.books.remove(book)
                return
        raise ValueError(f"Книга с названием '{title}' не найдена")

    def find_books_by_author(self, author):
        return [book for book in self.books if book['author'] == author]

# Пример использования
library = Library()
library.add_book({'title': '1984', 'author': 'George Orwell', 'year': 1949})
library.add_book({'title': 'Animal Farm', 'author': 'George Orwell', 'year': 1945})
library.add_book({'title': 'Brave New World', 'author': 'Aldous Huxley', 'year': 1932})

print(library.find_books_by_author('George Orwell'))  # Найдет книги Orwell
library.remove_book('1984')  # Удалит книгу '1984'
print(library.books)  # Покажет оставшиеся книги