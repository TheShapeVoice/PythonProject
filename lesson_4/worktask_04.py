# Generator
#
# def generator():
#     x = 1
#     yield x
#     x += 1
#     yield x
#
# g = generator()
# print(next(g))
# print(next(g))


# def generator():
#     x = 1
#     while x < 14:
#         yield x
#         x += 2
#
# g = generator()
# for i in g:
#     print(i)

# def generator():
#     x = 1
#     while x < 14:
#         yield x
#         x += 2
#
# g = generator()
# a = list(range(4, 10))
# print(a)

"""
Последовательность Фиббоначи
1 2 3 5 8 13 21 34 55 89 . . .
"""
# def fibonachi(xtrems):
#     x1 = 0
#     x2 = 1
#     count = 0
#
#     if xtrems <= 0:
#         print("укажите целое число")
#     elif xtrems == 1:
#         print("Последовательность фибоначчи", xtrems, ":")
#         print(x1)
#     else:

# a = [2, 4, 6, 8, 10, 12]
# b = []
# for elem in a:
#     b.append(elem*2)
# b = [elem*2 for elem in a] # лист комплихеншен генератор списка
# print(b)

# inp = (elem*2 for elem in a)
# inp = list(elem*2 for elem in a)
# print(inp)
# print(next(inp))
# print(next(inp))
# print(next(inp))

"""
Импортирвание модулей
"""


