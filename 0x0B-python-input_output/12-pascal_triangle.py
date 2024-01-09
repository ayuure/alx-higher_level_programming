#!/usr/bin/python3
"""This is a function"""


def pascal_triangle(n):
    """Function that prints pascal triangle"""
    triangle = []
    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        triangle.append(row)
    return triangle