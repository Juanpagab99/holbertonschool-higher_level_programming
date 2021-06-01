#!/usr/bin/python3
"""
MyList class
"""


class MyList(list):
    def print_sorted(self):
        """ Sorted """
        print(sorted(self))
