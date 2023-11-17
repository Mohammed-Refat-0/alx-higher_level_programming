def square_matrix_simple(matrix=[]):
    newmatrix = []
    for c in matrix:
        cnew = list(map(lambda x: x**2, c))
        new_matrix.append(cnew)
    return newmatrix
