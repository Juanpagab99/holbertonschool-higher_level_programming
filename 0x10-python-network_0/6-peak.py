#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Find peak function"""
    l = list_of_integers
    try:
        new = sorted(l)
        return new[-1]
    except:
        pass
