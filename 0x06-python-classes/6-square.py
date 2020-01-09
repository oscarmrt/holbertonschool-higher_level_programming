#!/usr/bin/python3
class Square:
    """creating a Private instance attribute: size"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

    def my_print(self):
        if self.__size == 0:
            print('')
        else:
            for x in range(self.__size):
                for z in range(self.__position[0]):
                    print(' ', end='')
                for y in range(self.__size):
                    print('#', end='')
                print('')

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if type(value) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(self.__position) is not 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if value <= 0:
            raise TypeError('position must be a tuple of 2 positive integers')
