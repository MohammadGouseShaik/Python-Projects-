def matrix_addition(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return "Error: Matrices are not the same size"
    else:
        result = [[0 for i in range(len(matrix1[0]))] for j in range(len(matrix1))]
        for i in range(len(matrix1)):
            for j in range(len(matrix1[0])):
                result[i][j] = matrix1[i][j] + matrix2[i][j]
        return result