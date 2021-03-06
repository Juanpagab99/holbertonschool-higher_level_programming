#!/usr/bin/python3
"""
This module contains
the Base Class
"""
import json


class Base:
    """ Class that initializate
    an object """
    __nb_objects = 0

    def __init__(self, id=None):
        """ avoid duplicating
        the same code """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ JSON string
        representation """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Writes the JSON string representation of list_objs to a file.
        """
        content = []
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            content = []
            for i in list_objs:
                content.append(cls.to_dictionary(i))

        with open(filename, 'w') as f:
            f.write(cls.to_json_string(content))

    def from_json_string(json_string):
        """ returns the list
        of the JSON string
        representation """
        if json_string is None:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Create """
        if cls.__name__ is "Rectangle":
            tmp = cls(3, 1)
        else:
            tmp = cls(6)
        tmp.update(**dictionary)
        return tmp

    @classmethod
    def load_from_file(cls):
        """ Load from file"""
        try:
            with open(cls.__name__ + ".json", "r") as out_file:
                c = cls.from_json_string(out_file.read())
                aux = []
                for i in c:
                    aux.append(cls.create(**i))
                return aux
        except FileNotFoundError:
            return []
