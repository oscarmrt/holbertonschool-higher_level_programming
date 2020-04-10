#!/usr/bin/python3


def find_peak(list_of_integers):
    '''function that finds a peak in a list of unsorted integers.'''
    lessP = []
    equalP = []
    greaterP= []
    if len(list_of_integers) > 1:
        pvt = list_of_integers[0]
        for x in list_of_integers:
            if x < pvt:
                lessP.append(x)
            elif x == pvt:
                equalP.append(x)
            elif x > pvt:
                greaterP.append(x)
        if len(greaterP) > 1:
            return max(greaterP)
        else:
            return pvt
    else:
        return None
