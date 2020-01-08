#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ct = 0
    for y in my_list[0:x]:
        try:
            print('{:d}'.format(y), end='')
            ct += 1
        except (TypeError, ValueError):
            pass
    print()
    return (ct)
