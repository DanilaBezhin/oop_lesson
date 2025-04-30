# raise - генерирует исключение 
# для raise нужно прописывать класс исключения, которое вы хотите генерировать

# BaseException - базовый класс всех исключений 


# Пример класса, для печати данных на принтаре 

class ExceptionPrint(Exception):
    """Общий класс исключений для печати данных на принтере"""

class ExceptionPrintSendDate(ExceptionPrint):
    """Класс исключения для печати данных на принтере"""
    def __init__(self, *args):
        self.message = args[0] if args else None 

    def __str__(self):
        return f"Ошибка {self.message}"

class PrintData:
    def print(self, date):
        self.send_data(date)
        print(f"печать: {date}")

    def send_data(self, data):
        if not self.send_to_print(data):
            # обычно так, поскольку Exception является базовым классом для многих исключений 
            # raise Exception("принтер не отвечает")
            # но можем реализовать собственное исключение
            raise ExceptionPrintSendDate("принтер не отвечает")

    def send_to_print(self, data):
        return False 

    
p = PrintData()


# Учитываем иерархию исключений
try:
    p.print('2020-01-01')
except ExceptionPrintSendDate as e:
    print(e)
except ExceptionPrint as e:
    print(e)