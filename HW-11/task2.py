# Создайте класс Матрица. Добавьте методы для: вывода на печать, проверку на равенство, сложения, *умножения матриц
class Matrix:
    '''Класс матрица с инициализацией списка списков с
     методами сложения, умножения, сравнения на равенство и строчного вывода.'''

    def __init__(self, my_matrix: list[list[int]]):
        self.my_matrix = my_matrix

    def __str__(self):
        result = ''
        for row in self.my_matrix:
            for item in row:
                result += ''.join(f'{item}\t')
            result += ''.join('\n')
        return result

    def __eq__(self, other):
        '''Метод для сравнения матриц на равенство.'''
        return True if self.my_matrix == other.my_matrix else False

    def __add__(self, other):
        '''Метод сложения матриц.'''
        result = []
        row = []
        for i in range(len(self.my_matrix)):
            for j in range(len(self.my_matrix[0])):
                row.append(self.my_matrix[i][j] + other.my_matrix[i][j])
            result.append(row)
            row = []
        return Matrix(result)

    def __mul__(self, other):
        '''Метод умножения матриц.'''
        m = len(self.my_matrix)
        n = len(other.my_matrix)
        k = len(other.my_matrix[0])
        result = [[0 for _ in range(k)] for _ in range(m)]
        for i in range(m):
            for j in range(k):
                result[i][j] = sum(self.my_matrix[i][k] * other.my_matrix[k][j] for k in range(n))
        return Matrix(result)

    def __repr__(self):
        return f'{type(self).__name__}([[5, 5, 5], [6, 6, 6], [7, 7,7]])'

if __name__ == '__main__':
    matrix_1 = Matrix([[5, 5, 5], [4, 4, 4], [3, 3, 3]])
    matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print( matrix_1)
    print('*' * 10)
    print(matrix_2)
    print('*' * 10)

    print('Сложение матриц:')
    print(matrix_1.__add__(matrix_2))

    print('Умножение матриц:')
    print(matrix_1.__mul__(matrix_2))

    print(f'Сравнение: {matrix_1 == matrix_2}')
    print('*' * 10)

    print(repr(matrix_1))
    print('*' * 20)
    print(matrix_1.__doc__)
    print('*' * 20)
    help(matrix_2)

