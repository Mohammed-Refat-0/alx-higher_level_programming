def square_matrix_simple(matrix=[]):
    newmatrix = matrix.copy()
    for i in range(len(newmatrix)):
        newmatrix[i] = list(map(lambda x: x**2, newmatrix[i]))
