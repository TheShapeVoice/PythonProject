# Task 5

proceeds = int(input("Введите значение выручки: "))
cost = int(input("Введите значение издержек: "))
if proceeds > cost:
    print("Фирма работает в прибыль")
    print("Рентабельность составляет %.2f" % (proceeds / cost * 100),"%")
    people = int(input("Введите численность сотрудников фирмы: "))
    cost_for_people = proceeds / people
    print("Прибыль в рассчете на 1 человека состовляет - %.2f" % cost_for_people)

elif proceeds < cost:
    print("Фирма работает в убыток")

else:
    print("Фирма отработала в ноль")