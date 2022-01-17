# Task 3 Вариант 1

def my_func(a, b, c):
    if a > b and b > c:
        result = a + b
        return result
    if a < b and a > c:
        result_1 = a + c
        return result_1
    if a < b and a < c:
        result_2 = b + c
        return result_2
    if a > b and b < c:
        result_3 = a + c
        return result_3
    else:
        result_4 = a + b
        return result_4

finish_result = my_func(10, 5, 3)
print(finish_result)

# Task 3.1 Вариант 2 не сразу понял как его правильно написать, разбор на уроке помог понять, как синтаксис правильно
# написать в функции. Запутался как правильно написать разворот листа в функции.

def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.sort(reverse=True)
    return sum(my_list[:2])

print(my_func(2, 5, 19))