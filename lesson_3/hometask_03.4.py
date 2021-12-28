# Task 4 Вариант с возведением в степень через **
# def my_func(x: float, y: int):
#     if y < 0:
#         deg = 1 / (x**abs(y))
#         return deg
#     elif y == 0:
#         return 1
#     elif y > 0:
#         return "'Y' не может быть положительным числом"
# print(my_func(2.5, -5))

# Task 4.1 Возведение в степень через цикл. Подсмотрел в разборе ДЗ

def my_func(x: float, y: int):
    deg = 1
    while y < 0:
        deg *= 1 / x
        y += 1
    return deg
print(my_func(2, -2))