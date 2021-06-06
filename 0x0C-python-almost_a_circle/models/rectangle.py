#!/usr/bin/python3
""" This module contains
a Rectangle class """
from models.base import Base


class Rectangle(Base):
    """ Make a Rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializate """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
