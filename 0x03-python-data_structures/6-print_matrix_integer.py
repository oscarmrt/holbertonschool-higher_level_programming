#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not (len(matrix) == 1 and len(matrix[0]) == 0):
        for x in matrix:
            for y, element in enumerate(x):
                if (y + 1) != len(x):
                    print('{:d} '.format(element), end='')
                else:
                    print('{:d}'.format(element))
    else:
        print('')
