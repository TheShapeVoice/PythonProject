# Task 1

matrix_1 = [[1, 2, 2], [2, 2, 3], [6, 3, 4]]
matrix_2 = [[3, 1, 2], [6, 8, 3], [4, 1, 1]]


class Matrix:

    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        str_1 = '\n'
        for i in self.my_list:
            for j in i:
                str_1 += f'{j:4}'
            str_1 += '\n'
        return str_1

    def __add__(self, other):
        alf = []
        for i in range(len(self.my_list)):
            bet = []
            for j in range(len(self.my_list[i])):
                bet.append(self.my_list[i][j] + other.my_list[i][j])
            alf.append(bet)

        return Matrix(alf)

result_1 = Matrix(matrix_1)
result_2 = Matrix(matrix_2)
print(result_1 + result_2)