# Task 1

first_list = [1, 2.3, 'a', True, 3.23333, 2, 2, 'sdfg', 234, 'asdf', [1, 2, 3, 4], {1, 'ssdfsd', 234}]
j = 0
i = 0
while i < len(first_list):
    print("Элемент списка [%d] -" % j, type(first_list[i]))
    i += 1
    j += 1