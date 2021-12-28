# Task 6 Функцию для 1-го слова написал.. а вот для списка не сообразил.. тяжко что-то с ДЗ совсем.
#
def int_func(word):
    small_word = word.lower()
    return small_word.capitalize()

# print(int_func(input("Введите слово: ")))

letter_input = input("Введите слово: ")
letter_list = []
letter = letter_input.split()
for el in letter:
    letter_list.append(int_func(el))
print(" ".join(letter_list))
