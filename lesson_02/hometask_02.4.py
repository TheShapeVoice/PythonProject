# Task 4

first_string = input("Введите текст: ")
list_string = first_string.split()
i = 1
for words in list_string:
    print("Слово", i, words[:10])
    i += 1