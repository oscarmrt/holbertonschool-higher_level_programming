#!/usr/bin/python3
""" student module
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        n_dict = {}
        for x in attrs:
            try:
                n_dict[x] = self.__dict__[x]
            except:
                pass
        return n_dict

    def reload_from_json(self, json):
        for key, value in json.items():
            self.__dict__[key] = value
