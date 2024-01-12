#!/usr/bin/python3
""" base_model.py """
import uuid
from datetime import datetime
from . import storage


class BaseModel:
    """ BaseModel """

    def __init__(self, *args, **kwargs):
        """ __init__ """
        if not kwargs:
            self.id = str(uuid.uuid4())
            current_time = datetime.now()
            self.created_at = current_time
            self.updated_at = current_time
            storage.new(self.to_dict)
        else:
            for key in kwargs:
                if key == "created_at ":
                    self.created_at = datetime.fromisoformat(kwargs[key])
                    continue
                if key == "updated_at ":
                    self.updated_at = datetime.fromisoformat(kwargs[key])
                    continue
                if key != "__class__":
                    self.__setattr__(key, kwargs[key])

    def __str__(self):
        """ __str__ """
        return ("[{}] ({}) {}"
                .format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ save """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ to_dict """
        dictionary = self.__dict__
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat("T", "auto")
        dictionary["updated_at"] = self.updated_at.isoformat("T", "auto")
        return dictionary
