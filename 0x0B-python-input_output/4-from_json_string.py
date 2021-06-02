#!/usr/bin/python3
""" This function convert
JSON to python """


import json


def from_json_string(my_str):
    """ JSON representation """
    return json.loads(my_str)
