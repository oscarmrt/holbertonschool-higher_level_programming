#!/usr/bin/python3


def find_peak_aux(intList, low, high, n):
    '''auxiliar function to find index of middle element'''
    mid = int(low + (high - low) / 2)

    if ((mid == 0 or intList[mid - 1] <= intList[mid]) and
       (mid == n - 1 or intList[mid + 1] <= intList[mid])):
        return intList[mid]
    elif (mid > 0 and intList[mid - 1] > intList[mid]):
        return find_peak_aux(intList, low, (mid - 1), n)
    else:
        return find_peak_aux(intList, (mid + 1), high, n)


def find_peak(list_of_integers):
    '''function that finds a peak in a list of unsorted integers'''
    n = len(list_of_integers)
    if n == 0:
        return None
    elif n == 1:
        return list_of_integers[0]
    else:
        return find_peak_aux(list_of_integers, 0, n - 1, n)
