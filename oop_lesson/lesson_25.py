# Множественное наследование - когда класс наследуется от нескольких базовых классов

class Product:
    def __init__(self, name, weight, price):
        # вызывается именно следующий инициализатор по MRO
        super().__init__()
        self.name = name
        self.weight = weight
        self.price = price

    def get_info(self):
        return f'Product {self.name}, {self.price}, {self.weight}'

# Независимый базовый класс - миксин (примесь)
class MixinLog:
    id = 0

    def __init__(self):
        print(f'init MIxinLog, ID: {self.id}')
        self.__class__.id += 1
        self.ID = self.__class__.id

    def sell_log(self):
        print(f'{self.ID} был продан в 00:00, по цене {self.price}')

    def get_info(self):
        return f'Mixin {self.name}, {self.price}, {self.weight}'

class Notebook(Product, MixinLog):
    #В том случае если метод определен в обоих базовых классах, 
    # можно явно указать из какого класса нам нужно его вызвать
    def get_info(self):
        return MixinLog.get_info(self) 


n1 = Notebook('Acer', 1.5, 800)
n2 = Notebook('Asus', 1.2, 600)

print(n1.get_info())

n1.sell_log()
n2.sell_log()

# MRO - method resolution order - алгоритм обхода базовых классов при множественном наследовании 
# порядок зависит от порядка передачи базовых классов в  класс наследник 
print(Notebook.__mro__)


# Миксин - это класс, который:
# Не предназначен для создания самостоятельных экземпляров
# Содержит набор методов и атрибутов для добавления функциональности
# Используется вместе с другими классами через множественное наследование

# Отличия от обычных классов:
# Миксины обычно небольшие и узкоспециализированные
# Они не представляют самостоятельную сущность предметной области
# Их цель - расширять функциональность других классов