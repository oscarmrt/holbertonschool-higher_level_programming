#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[row * row for row in i] for i in matrix[:]]
    return new_matrix
