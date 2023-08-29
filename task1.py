
class Transport(object):
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Autobus(Transport):
    def print(self):
        print(f"Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}")

a = Autobus("Renaul Logan", 180, 12)
a.print()
