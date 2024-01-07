#!/usr/bin/python3
"""Function to divide a matrix"""


def matrix_divided(matrix, div):
    """Div matrix"""
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError ('Each row of the matrix must have the same size')
    if div == 0:
        raise ZeroDivisionError ('division by zero')
    if not isinstance(div, (int, float)):
        raise TypeError ('div must be a number')
    new_matrix = [[round(element /div, 2)for element in row]for row in matrix]
    return new_matrix