#!/usr/bin/python3
""" import tast_basemodel  """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class State_Test(test_basemodel):
    """ inherits from the test_basemodel class """

    def __init__(self, *args, **kwargs):
        """ overrides the __init__ method to set name and value """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def Test_Name(self):
        """ creating a new instance of the class and checking that name is a string """
        new = self.value()
        self.assertEqual(type(new.name), str)
