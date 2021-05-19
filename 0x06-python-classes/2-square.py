#!/usr/bin/python3
'''Class Square'''
class Square():
    '''Defines a square.
        Attributes:
        sizes: siza of a square
        error:
        TypeError - size must be an integer
        ValueError - size must be >= 0
        '''
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
