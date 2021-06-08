#!/usr/bin/python3
""" Square class """


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
