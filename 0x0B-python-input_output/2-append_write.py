#!/usr/bin/python3
""" This function appends a
string at the end of a text file """


def append_write(filename="", text=""):
    """append to file"""
    with open(filename, 'a') as f:
        lines = f.write(text)
        return lines
