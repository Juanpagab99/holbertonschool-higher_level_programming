#!/usr/bin/python3
"""
BaseGeometry class
"""


class BaseGeometry:
    """ two public instances methods """
    def area(self):
        """ Raise and exception """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """ verify value """
        if type(value) != int:
            raise TypeError("<name> must be an integer")
        elif value <= 0:
            raise ValueError("<name> must be greater than 0")
