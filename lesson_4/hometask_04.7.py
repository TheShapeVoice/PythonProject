# Task 7

from math import factorial

n = int(input("Введите число: "))
def fact():
    for i in range(0, n + 1):
        a = factorial(i)
        yield f'{i}! = {a}' # подсмотрел дял читаемости по красивее

for el in fact():
    print(el)

