# Паттерн "Моносостояние"
# Идея - есть многопоточный процесс, в каждом потоке создается свой экземпляр класса  
# но нам бы хотелось что бы все экземпляры имели единые локальный свойства 
# таким образом, что бы они были общими для всех экземпляров класса и изменение любого из них
# внутри какого либо экземпляра отражалось и в других экземплярах 

class ThreadData:
    # общие свойства для объектов 
    __shared_attrs = {
        'name': 'thread_1',
        'data': {
            'key_1': 'value_1',
            'key_2': 'value_2',
            'key_3': 'value_3',
        },
        'id': 1
    }

    def __init__(self):
        # ссылаемся на словарь __shared_attrs
        self.__dict__ = self.__shared_attrs

th1 = ThreadData()
th2 = ThreadData()

# изменяя name он меняется везде, как и задумано 
th1.name = 'thread_all'

# можно добавлять новые свойства, сразу везде
th1.original = True

print(th1.__dict__)
print(th2.__dict__)








# Задача: Управление глобальными настройками приложения
# Создайте класс AppSettings, который будет хранить настройки приложения.
# Требования :

# Все экземпляры класса AppSettings должны использовать одни и те же данные (настройки).
# При изменении настройки через один экземпляр, изменения должны отражаться во всех остальных.
# Должна быть возможность добавлять новые настройки через любой экземпляр.
# settings1 = AppSettings()
# settings2 = AppSettings()

# Установка настройки через первый экземпляр
# settings1.theme = "dark"
# settings1.language = "en"
# settings1.user_preferences = {
#     "notifications": True,
#     "sound": "high"
# }

# Проверка через второй экземпляр
# print(settings2.theme)  # "dark"
# print(settings2.user_preferences["sound"])  # "high"

# Изменение вложенной структуры через второй экземпляр
# settings2.user_preferences["sound"] = "mute"
# print(settings1.user_preferences["sound"])  # "mute"

# Добавление новой настройки через второй экземпляр
# settings2.version = "2.0.1"
# print(settings1.version)  # "2.0.1"



# Дополнительные задания

# Реализуйте метод reset_to_defaults :
# Метод должен сбрасывать все настройки до исходных значений.
# Пример:
# settings1.reset_to_defaults()
# print(settings2.theme)  # Значение по умолчанию (например, "light")


# Обработка вложенных изменяемых объектов :
# Убедитесь, что изменения внутри вложенных структур (например, user_preferences) влияют на все экземпляры.
# Пример:
# settings1.user_preferences["new_key"] = "test"
# print(settings2.user_preferences.get("new_key"))  # "test"


class AppSettings:
    __shared_attrs = {
        'theme': 'light',
        'language': 'en',
        'user_preferences': {
            'notifications': True,
            'sound': 'high'
        },
        'version': '1.0.0'
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs
        self.__dict__['v1'] = self.__shared_attrs.copy()


    def reset_to_defaults(self):
        print(self.__shared_attrs['v1'])
        self.__shared_attrs.update(self.__shared_attrs['v1'])

settings1 = AppSettings()
settings2 = AppSettings()
print(settings1.theme)  
print(settings2.theme)  

settings1.theme = 'black'
print(settings1.theme)  
print(settings2.theme)  

settings2.reset_to_defaults()
print(settings1.theme)  
print(settings2.theme)  


# Ответить на вопросы по теме
# 1 Что такое паттерн моносостояние, а  так же дать 3 примере, для чего он может пригодится 
# 2 Что мы получим обратившись к self.__dict__
# 3 Чем отличается приватный и защищенный метод 
# 4 Что такое classmethod и staticmethod 
# 5 Что будет есть написать raise AttributeError
# 6 Чем __getattr__ отличается от __getattribute__