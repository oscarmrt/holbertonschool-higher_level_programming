#!/usr/bin/python3
""" class Base
"""


import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """ init function
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ to_json_string function
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries = []
        return json.dumps(list_dictionaries)
