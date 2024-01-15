#!/usr/bin/python3
""" file_storage.py """

import json


class FileStorage:
    """ FileStorage """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ all """
        return (FileStorage.__objects)

    def new(self, obj):
        """ new """
        FileStorage.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """ save """
        if FileStorage.__file_path != None:
            with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
                temp = {}
                for key in FileStorage.__objects.keys():
                    temp[key] = FileStorage.__objects[key].to_dict()
                json_string = json.dumps(temp)
                f.write(json_string)

    def reload(self):
        """ reload """
        from models.base_model import BaseModel

        FileStorage.__objects = {}
        if FileStorage.__file_path == None:
            return ([])
        try:
            with open(FileStorage.__file_path, 'r') as f:
                json_string = f.read()
                if json_string is None or len(json_string) == 0:
                    return ([])
                dictionary = json.loads(json_string)
                for obj_id in dictionary.keys():
                    if "BaseModel" in obj_id:
                        BaseModel(**dictionary[obj_id])
            return (FileStorage.__objects)
        except FileNotFoundError as err:
            return ([])
