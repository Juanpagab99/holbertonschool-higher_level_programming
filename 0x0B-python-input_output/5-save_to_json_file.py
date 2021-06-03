#!/usr/bin/python3
""" This function writes
an Object to a text file """


import json


def save_to_json_file(my_obj, filename):
    """ JSON representation """
    with open(filename, 'w') as f:
        json.dumps(my_obj, f)
