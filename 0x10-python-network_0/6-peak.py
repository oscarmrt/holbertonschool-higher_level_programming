#!/usr/bin/python3


def find_peak(list_of_integers):
    '''function that finds a peak in a list of unsorted integers.'''
    list = list_of_integers
    if list == []:
        return None
    peak = max(list)
    return peak
