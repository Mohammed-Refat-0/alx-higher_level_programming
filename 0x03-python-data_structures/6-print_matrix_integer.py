#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in row:
            print("{:d}".format(elem), end=" " if i != row[-1] else "")
        print()
