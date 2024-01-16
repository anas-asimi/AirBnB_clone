#!/usr/bin/python3
""" import tast_basemodel """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class User_Test(test_basemodel):
    """ inherits from the test_basemodel class """

    def __init__(self, *args, **kwargs):
        """ overrides the __init__ method to set name and value """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ Creates a new instance of the City class and checks that its first_name attribute is a string """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ Creates a new instance of the City class and checks that its last_name attribute is a string """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ Creates a new instance of the City class and checks that its email attribute is a string """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ Creates a new instance of the City class and checks that its password attribute is a string """
        new = self.value()
        self.assertEqual(type(new.password), str)
