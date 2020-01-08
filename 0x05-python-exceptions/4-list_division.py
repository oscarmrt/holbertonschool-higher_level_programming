#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    res = 0
    for x in range(list_length):
        try:
            res = my_list_1[x] / my_list_2[x]
        except TypeError:
            print('wrong type')
            res = 0
        except ZeroDivisionError:
            print('division by 0')
            res = 0
        except IndexError:
            print('out of range')
            res = 0
        finally:
            new_list.append(res)
    return new_list
