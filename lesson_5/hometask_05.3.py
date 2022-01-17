# Task 3 Подсмотрел - не сам решил. Что-то как-то сложно, не усвоился материал предыдущий

with open("task_3.txt", "r", encoding="utf-8") as task3:
    i = {a.split()[0]: float(a.split()[1]) for a in task3}
    b = {el[0] for el in i.items() if el[1] < 20000}
    print(f'Сотрудник, чей оклад меньше 20т.р. -', *b)
    print(f'Средняя величина дохода = {round(sum(i.values()) / len(i), 2)}')
