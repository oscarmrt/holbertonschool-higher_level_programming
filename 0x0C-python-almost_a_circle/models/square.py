#!/usr/bin/python3
from models.rectangle import Rectangle
""" class Square
"""


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value <= 0:
            raise ValueError('size must be > 0')
        self.__size = value

    def __str__(self):
        return ('[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y,
                self.__size))
