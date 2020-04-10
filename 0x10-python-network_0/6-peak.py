#!/usr/bin/python3


def find_peak(list_of_integers):
    '''function that finds a peak in a list of unsorted integers'''
    n = len(list_of_integers)
    high = n - 1
    low = 0
    mid = int((low + high) / 2)

    if n == 0:
        return None
    elif n == 1:
        return list_of_integers[0]
    else:
        while (low < high):
            if (list_of_integers[mid] > list_of_integers[mid + 1]):
                high = mid
            else:
                low = mid + 1
        return list_of_integers[low]
