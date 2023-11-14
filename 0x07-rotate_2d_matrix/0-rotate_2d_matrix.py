#!/usr/bin/python3
"""
rotates a n x n 2D matrix 90degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    2-dimension
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()

    return matrix
