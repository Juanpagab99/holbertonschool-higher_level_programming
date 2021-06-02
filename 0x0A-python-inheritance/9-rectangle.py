#!/usr/bin/python3
""" Rectangle class """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle"""

    def __init__(self, width, height):
        """Initializate"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate area """
        return self.__width * self.__height

    def __str__(self):
        """return the following rectangle """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
