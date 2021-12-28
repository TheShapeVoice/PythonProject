# Task 2 Вариант с вводом данных от пользователя

def about_user():
    name = input("Введите имя: ")
    surname = input("Введите фамилия: ")
    years = input("Введите год рождения: ")
    city = input("Введите город проживания: ")
    email = input("Введите ваш email: ")
    phone_number = input("Введите номер телефона: ")
    all_info = "Имя: %s" % name + ', ' + "Фамилия: %s" % surname + ', ' + "Год: %s" % years + ', ' + \
               "Город: %s" % city + ', ' + "Почта: %s" % email + ', ' + "Телефон: %s" % phone_number

    return all_info

result = about_user()
print(result)

# Task 2.1 Вариант через именнованный аргумент. Если честно не совсем понимаю как работает. Взял с разбора ДЗ.
# Пока писал, вроде что то дошло как работает.

def about_user(**kwargs):
    return f"Имя: {kwargs['name']}, Фамилия: {kwargs['surname']}, Год: {kwargs['year']}, Город: {kwargs['city']}, " \
           f"Почта: {kwargs['email']}, Телефон: {kwargs['phone']}"

print(about_user(name='Антон', surname='Васильев', year='1988', city='Спб', email='1@1.ru', phone='+79523322256'))