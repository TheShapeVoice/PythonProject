# Task 2 Не сам решал. Подсмотрел как реализовано. Не совсем закрепились предыдущие материалы.

with open("task_2.txt", encoding="utf-8") as task2:
    my_lines = task2.readlines()
    my_strings = [f'Строка {a} - содержит {len(b.split())} слова'for a, b in enumerate(my_lines, 1)]
    print(*my_strings, sep="\n")
    print(f"В файле количество строк - {len(list(my_lines))} шт")

    print(my_lines)