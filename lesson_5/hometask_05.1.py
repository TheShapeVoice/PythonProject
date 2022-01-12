# Task 1

with open("task_1.txt", "w+", encoding="utf-8") as task_1:
    while True:
        task1_list = input("Введите данные (Для завершения оставьте пустую строку и нажмите Enter): ")
        if not task1_list:
            break
        print(task1_list, file=task_1)

