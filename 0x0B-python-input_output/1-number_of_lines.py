#!/usr/bin/python3
def number_of_lines(filename=""):
    ct = 0
    with open(filename, encoding='utf-8') as file:
        for line in file:
            ct += 1
        return ct
