# Task 2

class ZeroOwn(Exception):
    def __init__(self, text):
        self.text = text


class Division:

    def __init__(self):
        self.num_1 = input("Введите числитель: ")
        self.num_2 = input("Введите знаменатель: ")

    def div(self):
        try:
            self.num_1 = int(self.num_1)
            self.num_2 = int(self.num_2)
            if self.num_2 == 0:
                raise ZeroOwn("Делить на ноль запрещено!")
        except (ZeroDivisionError, ZeroOwn) as err:
            print(err)
        except ValueError:
            print("Вводить можно только целое число")
        else:
            print(f"Результат деления: {round(float(self.num_1 / self.num_2), 2)}")


task2 = Division()
task2.div()