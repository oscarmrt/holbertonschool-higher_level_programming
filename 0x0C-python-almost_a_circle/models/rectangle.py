#!/usr/bin/python3
from models.base import Base
""" class Rectangle
"""


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        if self.__width == 0 and self.__height == 0:
            print('')
        else:
            for k in range(self.__y):
                print('\n', end='')
            for i in range(self.__height):
                for l in range(self.__x):
                    print(' ', end='')
                for j in range(self.__width):
                    print('#', end='')
                print('')

    def __str__(self):
        return ('[Rectangle] ({}) {}/{} - {}/{}'.format(self.id,
                                                        self.__x,
                                                        self.__y,
                                                        self.__width,
                                                        self.__height))

    def update(self, *args, **kwargs):
        if args and args is not None:
            for idx, value in enumerate(args):
                if idx == 0:
                    self.id = value
                if idx == 1:
                    self.__width = value
                if idx == 2:
                    self.__height = value
                if idx == 3:
                    self.__x = value
                if idx == 4:
                    self.__y = value
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.__width = kwargs['width']
            if 'height' in kwargs:
                self.__height = kwargs['height']
            if 'x' in kwargs:
                self.__x = kwargs['x']
            if 'y' in kwargs:
                self.__y = kwargs['y']

    def to_dictionary(self):
        dictionary = {'id': self.id, 'width': self.__width,
                                     'height': self.__height,
                                     'x': self.__x, 'y': self.__y}
        return dictionary
