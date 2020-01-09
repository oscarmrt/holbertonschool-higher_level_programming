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
        if self.__size is not 0:
            for t in range(self.__position[1]):
                print('')
            for x in range(self.__size):
                for z in range(self.__position[0]):
                    print(' ', end='')
                for y in range(self.__size):
                    print('#', end='')
                print('')
        else:
            print('')

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if type(value) is not tuple or len(value) is not 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if any(type(i) is not int for i in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        if any(i < 0 for i in value):
            raise TypeError('position must be a tuple of 2 positive integers')
