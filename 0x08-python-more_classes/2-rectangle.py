#!/usr/bin/python3
class Rectangle:
    """Empty class Rectangle"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * self.__width + 2 * self.__height
