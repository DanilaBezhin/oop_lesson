# Итератор в Python — это объект, который поддерживает протокол итерации. 
# Проще говоря, итератор — это объект, который возвращает свои элементы по одному за раз. 
# В Python итераторы являются основой работы с циклами for и конструкциями, которые предполагают последовательный обход данных.

# Основные особенности итераторов:

# Протокол итератора: Итератор должен реализовывать два метода:
    # __iter__(): Возвращает сам итератор. Этот метод вызывается при начале итерации.

    # __next__(): Возвращает следующий элемент последовательности. 
    # При достижении конца последовательности должен вызвать исключение StopIteration.

# Создание итератора:
    # Итератор может быть создан вручную с помощью класса, который реализует методы __iter__() и __next__().

    # Стандартные объекты Python, такие как списки, кортежи, строки и словари, являются итерируемыми объектами. 
    # Для получения итератора из них используется функция iter().

# List, tuple, str, dict и sets, range — это все итерируемые объекты.
# my_tuple = ("яблоко", "банан", "вишня")
# my_it = iter(my_tuple)
# print(next(my_it))
# print(next(my_it))
# print(next(my_it))
# print(next(my_it)) # Ошибка - StopIteration


# магические методы __iter__ и __next__
# __iter__(self) - получение итератора для перебора объекта
# __next__(self) - переход к следующему значению и его считывание 

# range(start, stop, step) - арифметическая последовательность, которую можно перебрать с помощью итератора 

class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.value = self.start - self.step
        return self

    # для получения следующего значения арифметической последовательности 
    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration
        
fr = FRange(0, 2, 0.5)
# fr = iter(fr)

# благодаря реализации __next__ можем использовать next
# fr выступает в роли итератора 
# print(next(fr))
# print(next(fr))
# print(next(fr))
# print(next(fr))
# print(next(fr))


# что бы создать сам итератор нужно реализовать мг метод __iter__
# it = iter(fr)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# так же мы можем использовать перебор через for так как он не явно вызывает iter, а далее next перебирает 
# for i in fr:
#     print(i)


class FRange2D:
    def __init__(self, start=0.0, stop=0.0, step=1, rows=5):
        self.row = rows
        self.fr = FRange(start, stop, step)

    def __iter__(self):
        self.value = 0
        return self 
    
    def __next__(self):
        if self.value < self.row:
            self.value += 1
            return iter(self.fr)
        else:
            raise StopIteration
        

fr2 = FRange2D(0, 2, 0.5, 4)
for x in fr2:
    for y in x:
        print(y, end=" ")
    print()







# игра математическая викторина
import random
import time

def generate_question():
    """Генерирует случайный математический вопрос."""
    num1 = random.randint(1, 20)  # Первое число (простое)
    num2 = random.randint(1, 20)  # Второе число (простое)
    operation = random.choice(['+', '-', '*'])  # Случайная операция
    
    if operation == '+':
        answer = num1 + num2
    elif operation == '-':
        answer = num1 - num2
    elif operation == '*':
        answer = num1 * num2
    
    question = f"{num1} {operation} {num2}"
    return question, answer

def math_quiz():
    print("Добро пожаловать в Математический Квиз!")
    print("У вас будет 5 секунд на каждый ответ. Удачи!\n")
    
    score = 0
    total_questions = 5  # Общее количество вопросов
    time_limit = 5  # Время на ответ в секундах
    
    for i in range(total_questions):
        question, correct_answer = generate_question()
        print(f"Вопрос {i + 1}: {question}")
        
        start_time = time.time()  # Засекаем время начала
        
        try:
            user_input = input("Ваш ответ: ")
            elapsed_time = time.time() - start_time  # Считаем затраченное время
            
            if elapsed_time > time_limit:
                print(f"Время вышло! Правильный ответ был: {correct_answer}\n")
                continue
            
            user_answer = int(user_input)
            
            if user_answer == correct_answer:
                print("Правильно!\n")
                score += 1
            else:
                print(f"Неправильно! Правильный ответ: {correct_answer}\n")
        
        except ValueError:
            print("Некорректный ввод! Пропускаем этот вопрос.\n")
    
    print(f"Игра окончена! Ваш счет: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()