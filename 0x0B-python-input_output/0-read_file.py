#!/usr/bin/python3
""" This function reads a file """


def read_file(filename=""):
    """ with function to
    open and close .txt """
    with open(filename, 'r', encoding = "utf-8") as f:
        lines = f.read()
        print(lines)
