#!/usr/bin/python3
""" __init__.py """
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
listOfClasses = ["BaseModel", "User", "State",
                 "City", "Amenity", "Place", "Review"]
