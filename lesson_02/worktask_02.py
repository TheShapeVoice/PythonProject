# Числовой тип данных

a = -43.08
print(a)
print(int(a))
print(abs(a))


a = 43
print(bin(a)) # двоичная
print(oct(43)) # восьмиричная
print(hex(43)) # шестнадцатиричная

# побитовое

my_int = 43 | 7
print(my_int)


a = 14
print(a)
print(a + 15)

# коллекции данных

my_list = ['a', 'b', 'c', 'd', 'f']
my_list.append('j') # добавление в список 1 элемент
print(my_list)
my_list_2 = ['h', 'i']
my_list.extend(my_list_2)
print(my_list)
my_list.extend(['t', 'g']) # добавление в список списка
print(my_list)
my_list.insert(5, 'Q') # добавление в указанное место в списке
print(my_list)
my_list.remove('d') # удаление по значению из списка (1-ый из списка по заданномк значению)
print(my_list)
my_list.pop(4) # удаление по индексу из списка
print(my_list)

print(my_list.index('j'))
my_list.append('j')
print(my_list)
my_list.remove('j')
print(my_list)


my_list = [2, 3, 5, 7, 7, 8, 90, 5, 1, 12, 6]
my_list.sort()
print(my_list)

my_list = ["a", "aaa", "aa", "b", "bbb"]
my_list.sort(key=len)
print(my_list)

my_list = [2, 3, 5, 7, 7, 8, 90, 5, 1, 12, 6]
my_list.sort(reverse=False) # по возрастанию
print(my_list)
my_list.sort(reverse=True) # по убыванию
print(my_list)

my_list = ['a', 'b', 'c', 'd', 'f']
my_list_copy = my_list.copy()
print(my_list_copy)


print(list(enumerate(my_list)))

my_tuple = (2, 3, 3, 5, 6, 3, 3, 3, 3, 4) # кортеж
print(my_tuple.count(3)) # подсчет значений в кортеже

my_string = "Ехал Грека через Реку"
new_my_string = my_string.lower() # делает все буквы строчными
print(new_my_string)
my_string.upper() # делает все буквы заглавными

my_string.title() # делает каждый элемент с заглавной буквы

my_string.split() # разделяет слова (объекты) отдельно
new_my_string = my_string.split()
print(new_my_string)
words = (',').join(new_my_string)
print(words)

# Словарь
my_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4}
print(my_dict['Jan'])

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

print(my_dict.get('June'))
print(my_dict.get('Jan'))