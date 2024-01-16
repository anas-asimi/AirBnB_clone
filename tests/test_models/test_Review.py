#!/usr/bin/python3
""" import tast_basemodel """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class Review_Test(test_basemodel):
    """ inherits from the test_basemodel class """

    def __init__(self, *args, **kwargs):
        """ overrides the __init__ method to set name and value """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def Test_Place_id(self):
        """ Creates a new instance of the City class and checks that its place_id attribute is a string """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def Test_User_id(self):
        """ Creates a new instance of the City class and checks that its user_id attribute is a string """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def Test_Text(self):
        """ Creates a new instance of the City class and checks that its text attribute is a string """
        new = self.value()
        self.assertEqual(type(new.text), str)
