#!/usr/bin/python3
def uppercase(str):
    for characters in str:
        if ord(characters) >= 97 and ord(characters) <= 122:
            characters = chr(ord(characters) - 32)
        print('{:s}'.format(characters), end='')
    print('')
