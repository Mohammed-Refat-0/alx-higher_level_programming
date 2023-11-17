#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = []
    for c in matrix:
        cnew = list(map(lambda x: x**2, c))
        newmatrix.append(cnew)
    return newmatrix
