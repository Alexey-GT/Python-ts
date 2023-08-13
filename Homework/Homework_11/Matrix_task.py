class Matirx:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def __str__(self):
        matrix_str = ""
        for row in self.data:
            matrix_str += " ".join(str(element) for element in row) + "\n"
        return matrix_str

    def __eq__(self, other):
        if isinstance(other, Matirx):
            return self.data == other.data
        return False

    def __add__(self, other):
        if isinstance(other, Matirx) and self.rows == other.rows and self.cols == other.cols:
            result = Matirx(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.data[i][j] = self.data[i][j] + other.data[i][j]
            return result
        else:
            raise ValueError("Матрицы должны иметь одинаковый размер для сложенияпроне")

    def __mul__(self, other):
        if isinstance(other, Matirx) and self.cols == other.rows:
            result = Matirx(self.rows, other.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    for k in range(self.cols):
                        result.data[i][j] += self.data[i][k] * other.data[k][j]
            return result
        else:
            raise ValueError("Количество столбцов в первой матрице должно совпасть количеством строк во второй матрице")


matrix_1 = Matirx(2, 3)
matrix_1.data = [[1, 2, 3], [4, 5, 6]]

matrix_2 = Matirx(2, 3)
matrix_2.data = [[7, 8, 9], [10, 11, 12]]

matrix_3 = Matirx(2, 2)
matrix_3.data = [[1, 2], [3, 4]]

print(matrix_1)
print(matrix_2)
print(matrix_3)

print(matrix_1 == matrix_2)
print(matrix_1 + matrix_2)

matrix_4 = matrix_1 * matrix_3
print(matrix_4)
