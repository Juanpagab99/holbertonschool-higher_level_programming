#!/usr/bin/python3
"""
This module contains
a Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """ Make a Rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializate """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Property of
        width """
        return self.__width

    @width.setter
    def width(self, value):
        """ validation
        of width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Property of
        height """
        return self.__height

    @height.setter
    def height(self, value):
        """ validation
        of height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Property
        of x """
        return self.__x

    @x.setter
    def x(self, value):
        """ validation
        of x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Property
        of y """
        return self.__y

    @y.setter
    def y(self, value):
        """ validation
        of y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Return
        area """
        return self.__width * self.__height

    def display(self):
        """ Display
        rectangle """
        print((self.__y - 1) * "\n")
        for i in range(self.__height):
            print("{:s}{:s}".format(" " * self.__x, "#" * self.__width))

    def __str__(self):
        """ Return the format """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
        self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ That assigns an
        argument to each attribute """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ Dictionary """
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self. width
        }
