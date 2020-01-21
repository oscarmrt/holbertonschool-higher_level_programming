#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, encoding='utf-8') as file:
        ct = 0
        if nb_lines <= 0:
            print(file.read(), end='')
            return
        for ct, line in enumerate(file):
            if nb_lines == ct:
                break
            print(line, end='')
