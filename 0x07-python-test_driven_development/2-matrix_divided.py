#!/usr/bin/python3
"""matrix_divided module"""


def matrix_divided(matrix, div):
    """function that divide a matrix by a number

       Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.

    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.

    Returns:
        matrix
    """
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
