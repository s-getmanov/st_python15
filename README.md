# st_python15
## Стек технологий Python. Урок №15. ООП

### Задание №1
Есть родительский класс:

class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
 
Создайте объект Autobus, который унаследует все переменные и методы родительского класса Transport и выведете его.
Ожидаемый результат вывода:

Название автомобиля: Renaul Logan Скорость: 180 Пробег: 12

####  Файл к заданию 1: 
[task1.py](https://github.com/s-getmanov/st_python15/blob/main/task1.py)

### Задание №2

Создайте класс Autobus, который наследуется от класса Transport.

Дайте аргументу Autobus.seating_capacity() значение по умолчанию 50.

Используйте переопределение метода.

Используйте следующий код для родительского класса транспортного средства: 

class Transport:

   def __init__(self, name, max_speed, mileage):

self.name = name
self.max_speed = max_speed
self.mileage = mileage
 

   def seating_capacity(self, capacity):

       return f"Вместимость одного автобуса {self.name}  {capacity} пассажиров"

 

Ожидаемый результат вывода:

Вместимость одного автобуса Renaul Logan: 50 пассажиров


####  Файл к заданию 2: 
[task1.py](https://github.com/s-getmanov/st_python15/blob/main/task2.py)

