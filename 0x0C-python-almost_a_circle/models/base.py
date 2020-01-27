#!/usr/bin/python3
""" class Base
"""


import json


class Base:
    """class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init function
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to_json_string function
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save_to_file function
        """
        objct = []
        if list_objs is None:
            objct = []
        else:
            objct = [x.to_dictionary() for x in list_objs]
        objct = cls.to_json_string(objct)
        filename = cls.__name__ + '.json'
        with open(filename, "w") as file:
            file.write(objct)

    @staticmethod
    def from_json_string(json_string):
        """ from_json_string function
        """
        if json_string is None:
            return []
        return json.loads(json_string)
