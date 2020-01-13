#!/usr/bin/python3
"""
Module is: "2-matrix_divided".

Write a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """This function divides all elements of a matrix."""
    matrix_size = None
    if type(matrix) is not list:
        raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats')
    for i in matrix:
        if type(i) is not list:
            raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats')
        if matrix_size is None:
            matrix_size = len(i)
        elif matrix_size != len(i):
            raise TypeError('Each row of the matrix must have the same size')
        for x in i:
            if type(x) is not int and type(x) is not float:
                raise TypeError('matrix must be a matrix\
(list of lists) of integers/floats')
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div is 0:
        raise ZeroDivisionError('division by zero')

    return [[round(x / div, 2) for x in i] for i in matrix]
