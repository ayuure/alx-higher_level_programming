#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[column[i]**2 for i in range(3)] for column in matrix ]
    return new_matrix
