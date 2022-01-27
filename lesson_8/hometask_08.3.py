# Task 3
# import re
# elif num.lower() is re.search(r'[a-nqru-z]'): - не получилось регулярку сюда приткнуть((
# не уверен что правильно описан паттерн !((

class ListLettersError(Exception):
    def __init__(self):
        self.text = "Необходимо вводить только цифры!!!"


class ListNum:

    def num_list(self):
        s = []
        while True:
            in_list = input(f"Введите значение, для выхода введите 'stop': ").split()
            for num in in_list:
                if num.lower() == "stop":
                    print(s)
                    return s
                else:
                    try:
                        if num.isdigit():
                            s.append(int(num))
                        else:
                            raise ListLettersError
                    except ListLettersError as fatal:
                        print(fatal.text)
        print(s)


first_attempt = ListNum()
first_attempt.num_list()