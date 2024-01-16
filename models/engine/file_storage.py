#!/usr/bin/python3
""" file_storage.py """

import json


class FileStorage:
    """ FileStorage """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ all """
        return self.__class__.__objects

    def new(self, obj):
        """ new """
        self.__class__.__objects.update(
            {obj.__class__.__name__ + '.' + obj.id: obj})

    def save(self):
        """ save """
        if self.__class__.__file_path != None:
            with open(self.__class__.__file_path, 'w', encoding='utf-8') as f:
                temp = {}
                for key, value in self.__class__.__objects.items():
                    temp[key] = value.to_dict()
                json.dump(temp, f)

    def reload(self):
        """ reload """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        self.__class__.__objects = {}
        try:
            with open(self.__class__.__file_path, 'r') as f:
                dictionary = json.load(f)
                if dictionary:
                    for key, value in dictionary.items():
                        if "BaseModel" in key:
                            BaseModel(**value)
                        elif "User" in key:
                            User(**value)
                        elif "State" in key:
                            State(**value)
                        elif "City" in key:
                            City(**value)
                        elif "Amenity" in key:
                            Amenity(**value)
                        elif "Place" in key:
                            Place(**value)
                        elif "Review" in key:
                            Review(**value)
        except FileNotFoundError:
            pass
