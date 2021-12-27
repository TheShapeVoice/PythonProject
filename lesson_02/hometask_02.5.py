# Task 5 не смог решить. просто скопировал с разбора ДЗ. не смог сообразить. сложно. не понимаю.

number_list = [10, 8, 5, 5, 2]
number_list_copy = number_list.copy()

try:
    n = int(input("Введите число: "))
    if n > number_list[0]:
        number_list_copy.insert(0, n)
    elif n < number_list[-1]:
        number_list_copy.append(n)
    else:
        for rating in number_list:
            if n == rating:
                rating_index = number_list.index(rating)
                rating_count = number_list.count(rating)
                new_rating_index = rating_index + rating_count
                number_list_copy.insert(new_rating_index, rating)
                break
            elif n > rating:
                number_list_copy.insert(number_list.index(rating), n)
                break
            else:
                continue
except IndexError:
    print("Неверные входные данные")

print(number_list_copy)