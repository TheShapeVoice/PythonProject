# Task 4

first_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
task4 = [num for num in first_list if first_list.count(num) < 2]
print("Результат:", task4)