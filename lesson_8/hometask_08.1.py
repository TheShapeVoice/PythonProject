# Task 1

class Date:
    def __init__(self):
        self.date = input("Введите дату по формату дд.мм.гггг: ")


    @classmethod
    def new_date(cls):
        date_1 = list(map(int, cls().date.split('.')))
        return date_1
        # print('Выведеная строка в типе init {}.{}.{}'.format(*date_1))


    @staticmethod # С валидацией что то не получилось (((( что у меня не правильно тут ??
    def validate_date():
        try:
            if Date.new_date()[0] not in range(1, 32):
                raise ValueError('День введен некорректно!')
            elif Date.new_date()[1] not in range(1, 13):
                raise ValueError('Месяц введен некорректно!')
            elif Date.new_date()[2] not in range(0, 9999):
                raise ValueError('Год введен некорректно!')
        except ValueError as e:
            print(e)
        else:
            print("Дата провалидирована успешно")


my_date = Date()
print(f'Введеная дата {my_date.date} - тип строка')

print('Выведеная строка в типе init {}.{}.{}'.format(*Date.new_date()))

my_date.validate_date()