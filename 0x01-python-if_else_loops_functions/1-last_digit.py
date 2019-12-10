#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
txt = "Last digit of"
aux = "and is less than 6 and not 0"
if number < 0:
    number *= -1
    mod = number % 10
    mod *= -1
    number *= -1
else:
    mod = number % 10
if mod == 0:
    print('{:s} {:d} is {:d} and is 0'.format(txt, number, mod))
elif mod > 5:
    print('{:s} {:d} is {:d} and is greater than 5'.format(txt, number, mod))
else:
    print('{:s} {:d} is {:d} {:s}'.format(txt, number, mod, aux))
