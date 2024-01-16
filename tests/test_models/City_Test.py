#!/usr/bin/python3
""" import tast_basemodel """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class City_Test(test_basemodel):
    """ inherits from the test_basemodel class """

    def __init__(self, *args, **kwargs):
        """ overrides the __init__ method to set name and value """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def Test_State_id(self):
        """ Creates a new instance of the City class and checks that its state_id attribute is a string """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def Test_Name(self):
        """ Creates a new instance of the City class and checks that its name attribute is a string  """
        new = self.value()
        self.assertEqual(type(new.name), str)
