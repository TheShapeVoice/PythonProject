# Task 3 - LIST

num_month = int(input("Введите число месяца: "))
winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
i = num_month
if winter.count(i) == True:
    print("Сейчас зима")
elif spring.count(i) == True:
    print("Сейчас весна")
elif summer.count(i) == True:
    print("Сейчас лето")
elif autumn.count(i) == True:
    print("Сейчас осень")
else:
    print("Введите корректное число месяца!")

# Task 3.1 - DICT

num_month = int(input("Введите число месяца: "))
season = {'Зима': [1, 2, 12], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}

for j, i in season.items():
    if num_month in i:
        print("Сейчас", j)
        break
else:
    print("Введите корректный номер месяца")