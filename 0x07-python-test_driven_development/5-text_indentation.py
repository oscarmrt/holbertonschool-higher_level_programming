#!/usr/bin/python3
"""
Module is: "5-text_indentation".

Write a function that prints a text with 2 new lines after each
of these characters: ., ? and :
"""


def text_indentation(text):
    """This function prints a text with 2 new lines after each
    of these characters: ., ? and :"""
    if type(text) is not str:
        raise TypeError('text must be a string')
    alert = 0
    for x in text:
        if alert == 0:
            if x == ' ':
                continue
            else:
                alert = 1
        if alert == 1:
            if x == '.' or x == '?' or x == ':':
                print(x)
                print()
                alert = 0
            else:
                print(x, end='')
