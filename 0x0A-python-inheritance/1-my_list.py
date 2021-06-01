#!/usr/bin/python3
"""
MyList class
"""


class MyList(list):
    def print_sorted(self):
        """ list print sorted """
        print(sorted(self))
