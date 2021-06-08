#!/usr/bin/python3
"""
Square class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Define a rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializate """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Return de format """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """ Property
        of self """
        return self.width

    @size.setter
    def size(self, value):
        """ The value
        of size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ args & kwargs """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                    self.height = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.width = kwargs["size"]
                self.height = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ Dictionary """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
