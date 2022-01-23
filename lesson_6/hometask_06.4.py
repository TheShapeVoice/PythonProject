# task_4 Подсмотрел только использование выбора для поворота )) прикольная штука))
from random import choice

class Car:
    direction = ["прямо", "направо", "налево", "задним ходом"]
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f"Автомобиль: {self.name}, цвет: {self.color}.\nЭто полицейский автомобиль? {self.is_police}")


    def go(self):
        print(f"Автомобиль {self.name} поехал со скоростью {self.speed} км/ч")

    def stop(self):
        print(f"Автомобиль {self.name} остановился")

    def turn(self):
        print(f'Автомобиль {self.name} движется {choice(self.direction)}')

    def show_speed(self):
        return f"Автомобиль {self.name} движется со скоростью {self.speed}"


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f"{self.name} превышает скорость")
        else:
            super().show_speed()

class SportCar(Car):

    def max_sport_speed(self, max_speed):
        print(f"Максимальная скорость {max_speed} км/ч")

    def time_to_100(self, seconds):
        print(f"Разгон с 0 до 100 км/ч за {float(seconds)} секунды")

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f"{self.name} превышает скорость")
        else:
            super().show_speed()

class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=True)

    def armor(self):
        print(f"Автомобиль бронированый")


car_1 = TownCar(50, "красный", "Opel")
car_1.go()
car_1.show_speed()
car_1.turn()
car_1.stop()
print()

car_2 = SportCar(250, "желтый", "Ferrari")
car_2.go()
car_2.show_speed()
car_2.turn()
car_2.stop()
car_2.max_sport_speed(353)
car_2.time_to_100(4.35)
print()

car_3 = WorkCar(70, "черный", "Audi")
car_3.go()
car_3.show_speed()
car_3.turn()
car_3.stop()
print()

car_4 = PoliceCar(150, "черно-белый", "Ford")
car_4.go()
car_4.show_speed()
car_4.turn()
car_4.stop()
car_4.armor()