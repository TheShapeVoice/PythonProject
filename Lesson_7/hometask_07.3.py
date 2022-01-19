# Task 3     Не понимаю!!! возвращаем объект и как что(( 

class Cell:
    def __init__(self, cage):
        self.cage = int(cage)

    def __add__(self, other):
        return Cell(self.cage + other.cage)

    def __sub__(self, other):
        if self.cage - other.cage > 0:
            return Cell(self.cage - other.cage)

    def __mul__(self, other):
        return Cell(self.cage * other.cage)

    def __truediv__(self, other):
        return Cell(self.cage // other.cage)

    def make_order(self, argum):
        return (('*' * argum) + '\n') * (self.cage // argum) + '*' * (self.cage % argum)


cage_1 = Cell(11)
cage_2 = Cell(10)
# print(cage_1 + cage_2) # не понимаю, почему не выводится на печать, ведь я возврашаю значение. не понимаю((
# print(cage_1 - cage_2)
# print(cage_1 * cage_2)
# print(cage_1 // cage_2)

cage_3 = cage_1 + cage_2
print(cage_3)

print(cage_1.make_order(5))
print()
print(cage_3.make_order(2))