#!/usr/bin/python3
""" import tast_basemodel """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class Amenity_Test(test_basemodel):
    """ inherits from the test_basemodel class """

    def __init__(self, *args, **kwargs):
        """ overrides the __init__ method to set name and value """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def Test_Name(self):
        """ Creates a new instance of the City class and checks that its name attribute is a string """
        new = self.value()
        self.assertEqual(type(new.name), str)
