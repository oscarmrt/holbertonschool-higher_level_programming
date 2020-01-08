#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        ct = 0
        for y in my_list[0:x]:
            print('{}'.format(y), end='')
            ct += 1
        print()
        return (ct)
    except IndexError:
        print()
        return (ct)
