# Task 5

from functools import reduce

task5 = [i for i in range(100, 1001) if i % 2 == 0]
result = reduce(lambda a, b: a * b, task5)
print("Результат умножения всех четных чисел, равен:\n", result)


# Наверно так по лучше.. но, не знаю? как с оптимизацией. Наверно можно еще короче записать ??

# task5 = [i for i in range(100, 1001) if i % 2 == 0]
# print("Результат умножения всех четных чисел, равен:\n", reduce(lambda a, b: a * b, task5))