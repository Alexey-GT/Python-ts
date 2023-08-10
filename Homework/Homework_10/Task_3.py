#Задача о транспонировнии матрицы
class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def transpose(self):
        transposed = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                transposed.data[j][i] = self.data[i][j]
        return transposed

    def print_matrix(self):
        for row in self.data:
            print(row)


# Создание и заполнение исходной матрицы
matrix = Matrix(3, 4)
matrix.data = [[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12]]

# Транспонирование и вывод результата
transposed_matrix = matrix.transpose()
transposed_matrix.print_matrix()