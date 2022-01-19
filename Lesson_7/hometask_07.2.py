# Task 2 Подсмотрел. Сложная тема нужна изучать((

from abc import ABC, abstractmethod


class Clothers(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def consu(self):
        pass

    def __add__(self, other):
        result = (self.consu + other.consu)
        return f'Количество ткани на 1 костюм и 1 пальто уходит {round(result, 2)}'


class Coat(Clothers):

    @property
    def consu(self):
        return round(self.param / 6.5 + 0.5, 2)


class Suit(Clothers):

    @property
    def consu(self):
        return round(self.param * 2 + 0.2, 2)


my_coat = Coat(150)
print(my_coat.consu)

my_suit = Suit(80)
print(my_suit.consu)

print(my_suit + my_coat)