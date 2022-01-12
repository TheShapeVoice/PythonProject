# Task 5
from functools import reduce

with open("Task_5.txt", "w+", encoding="utf-8") as task5:
        task5_list_num = input("Введите данные: ")
        print(task5_list_num, file=task5)
        print(f'Сумма введенных чисел =', reduce(lambda a, b: a + b, [int(i) for i in task5_list_num.split()]))