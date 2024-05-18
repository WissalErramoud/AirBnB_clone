#!/usr/bin/python3
"""
FileStorage module
"""
import json


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__file_path, "w", encoding="utf-8") as f:
            objects_dict = {key: obj.to_dict() for key,
                            obj in self.__objects.items()}
            json.dump(objects_dict, f, indent=4)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                objects_dict = json.load(f)
                for key, value in objects_dict.items():
                    class_name = value["__class__"]
        except FileNotFoundError:
            pass
