#!/usr/bin/python3
""" This function returns
the number of characters written
"""


def write_file(filename="", text=""):
    """ create or overwrite
    a file a count characters"""
    with open(filename, 'w') as f:
        lines = f.write(text)
        return lines
