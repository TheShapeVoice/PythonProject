# Task 4  Подсмотрел решение, не сам... вроде звучит просто, а подобраться не смог, думал через zip
#  попровобвать, но столкнулся с трудностями зазипить списко с рус.названиями

rus_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("task4_1.txt", "w", encoding="utf-8") as task4_1:
    with open("task_4.txt", "r", encoding="utf-8") as task4:
        task4_1.writelines([i.replace(i.split()[0], rus_dict.get(i.split()[0])) for i in task4])

