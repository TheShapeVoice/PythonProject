# task_3

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"Доход": wage, "Премия": bonus}


class Position(Worker):
    def full_name(self):
        print(f"Полное имя сотрудника {self.name} {self.surname}")

    def get_total_income(self):
        print(f'Сумма дохода с учетом премии {sum(self._income.values())}')


worker_1 = Position("Peter", "Parker", "superhero", 10000, 333)
worker_1.full_name()
worker_1.get_total_income()