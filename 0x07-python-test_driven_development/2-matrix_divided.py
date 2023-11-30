#!/usr/bin/python3
def matrix_divided(matrix, div):
    if type(div) not in [float, int]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if type(row) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for element in row:
            element/div
