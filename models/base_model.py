""" base_model.py """
import uuid
from datetime import datetime


class BaseModel:
    """ BaseModel """

    def __init__(self):
        self.id = str(uuid.uuid4())
        current_time = datetime.now()
        self.created_at = current_time
        self.updated_at = current_time

    def __str__(self):
        """ __str__ """
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ save """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ to_dict """
        dictionary = self.__dict__
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat("T", "auto")
        dictionary["updated_at"] = self.updated_at.isoformat("T", "auto")
        return dictionary
