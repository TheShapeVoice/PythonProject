# Task 2

my_list = []
n = int(input("Введите длинну списка: "))
for i in range(0, n):
    p = input("Введите значения для списка: ")
    my_list.append(p)
print("Правильный порядок заполнения списка:", my_list)
l = len(my_list)
i = 0
while l % 2 != 0:
    if i == l - 1:
        break
    my_list[i], my_list[i+1] = my_list[i + 1], my_list[i]
    i += 2
    continue
while l % 2 == 0:
    if i == l:
        break
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    i += 2
    continue
print("Порядок с обменом соседних элементов: ", my_list)