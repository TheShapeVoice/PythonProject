# Task 1 Вариант с запросом у пользователя

def two_number():
    try:
        first_number = int(input("Введите первое число: "))
        second_number = int(input("Введите второе число: "))
        division = first_number / second_number
        return division
    except ZeroDivisionError:
        division = "Деление на ноль недопустимо!!!"
        return division

result = two_number()
print("Результат деления чисел равен:", result)

# Task 1.2 Вариант с позиционными аргументами

# def two_number(a, b):
#     try:
#         division = a / b
#         return division
#     except ZeroDivisionError:
#         division = "Деление на ноль недопустимо!!!"
#         return division
#     except TypeError:
#         division = "Частное может принимать только числа"
#         return division
#
# print("Результат:", two_number(2, 0))