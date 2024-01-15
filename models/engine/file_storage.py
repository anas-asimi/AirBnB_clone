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
                for key in self.__class__.__objects.keys():
                    temp[key] = self.__class__.__objects[key].to_dict()
                json.dump(temp,f)

    def reload(self):
        """ reload """
        from models.base_model import BaseModel

        self.__class__.__objects = {}
        # if self.__class__.__file_path == None:
        #     return ({})
        try:
            with open(self.__class__.__file_path, 'r') as f:
                dictionary = json.load(f)
                if dictionary:
                    for obj_id in dictionary.keys():
                        if "BaseModel" in obj_id:
                            BaseModel(**dictionary[obj_id])
            # return (self.__class__.__objects)
        except FileNotFoundError:
            pass
