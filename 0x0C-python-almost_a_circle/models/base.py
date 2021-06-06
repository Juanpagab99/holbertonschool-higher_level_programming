#!/usr/bin/python3
""" This module contains
the Base Class """


class Base:
    """ Class that initializate
    an object """
    __nb_objects = 0

    def __init__(self, id=None):
        """ avoid duplicating
        the same code """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
