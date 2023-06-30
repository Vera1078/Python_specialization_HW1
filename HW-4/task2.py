# Напишите функцию для транспонирования матрицы.


def print_matrix(m):
    for item in m:
        print(item)

def trans_matrix (matrix):
    temp = []
    for i in range(len(matrix[0])):
        temp_col = []
        for j in range(len(matrix)):
            temp_col.append(matrix[j][i])
        temp.append(temp_col)
    return temp


my_matrix = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4]]
print(print_matrix(my_matrix))
print('-------------------------')
print_matrix(trans_matrix(my_matrix))






















































