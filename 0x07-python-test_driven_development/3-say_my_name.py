#!/usr/bin/python3
"""
Module is: "3-say_my_name".

Write a function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """This function that prints My Name."""
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print('My name is {:s} {:s}'.format(first_name, last_name))
