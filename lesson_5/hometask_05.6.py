# Task 6 Не мое решение. подсмотрел. Сложно и непонятно((((((

dict = {}
with open("task_6.txt", "r", encoding="utf-8") as task6:
    for line in task6:
        name_sub, count_hours = line.split(':')
        sum_hours = sum(map(int, "".join([i for i in count_hours if i == ' ' or '9' >= i >= '0']).split()))
        dict[name_sub] = sum_hours
print(f"{dict}")