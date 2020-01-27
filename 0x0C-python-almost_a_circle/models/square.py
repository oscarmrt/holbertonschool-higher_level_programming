#!/usr/bin/python3
""" class Square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ class square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ init function
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ size function
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ size function setter
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value <= 0:
            raise ValueError('size must be > 0')
        self.__size = value

    def __str__(self):
        """ str function
        """
        return ('[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y,
                self.__size))

    def update(self, *args, **kwargs):
        """ update function
        """
        if args and args is not None:
            for idx, value in enumerate(args):
                if idx == 0:
                    self.id = value
                if idx == 1:
                    self.__size = value
                if idx == 2:
                    self.x = value
                if idx == 3:
                    self.y = value

        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.__size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """ to_dictionary function
        """
        dictionary = {'id': self.id, 'size': self.__size,
                                     'x': self.x, 'y': self.y}
        return dictionary
