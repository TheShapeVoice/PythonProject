# Task 1 Подсмотрел не сам решил. Пытаюсь разобраться в том как работает argv

from sys import argv

def example():
    try:
        a, b, c = map(float, argv[1:])
        print(f"salary: {round((a * b + c), 2)}")
    except ValueError:
        print("Введите 3 числа. Текст недопустим")

example()