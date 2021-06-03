#!/usr/bin/python3
"""
    Script that adds all arguments
    to a Python list,
    and then save them to a file.
"""
from sys import argv

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
filename = 'add_item.json'

try:
    f = load_from_json_file(filename)
except:
    f = []
finally:
    f.extend(argv[1:])
    save_to_json_file(f, filename)
