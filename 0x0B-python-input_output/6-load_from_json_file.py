#!/usr/bin/python3
""" This function creates
an Object from a “JSON file” """


import json


def load_from_json_file(filename):
    """ load from JSON """
    with open(filename, 'r') as f:
        return json.load(f)
