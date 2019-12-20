#!/usr/bin/python3
def roman_to_int(roman_string):
    conromin = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    val = 0
    if roman_string is not None or roman_string is str:
        for x in roman_string:
            if x in conromin.keys():
                val = val + conromin[x]
        return val
    else:
        return 0
