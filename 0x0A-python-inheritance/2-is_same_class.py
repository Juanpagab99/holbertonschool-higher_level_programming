#!/usr/bin/python3
""" This function returns
    True if the object is exactly
    an instance of the specified
    class ; otherwise False """


def is_same_class(obj, a_class):
    """ Verify if is int or not """
    if type(obj) == a_class:
        return True
    else:
        return False
