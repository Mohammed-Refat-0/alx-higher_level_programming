#!/usr/bin/python3
"""contain Base class
"""
import json


class Base:
    """base of all other classes in this project.
    to manage id attribute in all future classes
    and to avoid duplicating the same code and bugs
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor
        Args:
            id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [i.to_dictionary() for i in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string of list of objects.
        """
        if json_string is None or json_string == "[]":
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """return a class instantied from a dictionary of attributes
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """return a list of classes instantiated from a file of JSON strings
        """
        filename = str(cls.__name__) + ".json"
        with open(filename, "r") as jsonfile:
            list_dicts = Base.from_json_string(jsonfile.read())
            return [cls.create(**d) for d in list_dicts]
