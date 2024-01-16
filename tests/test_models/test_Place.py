#!/usr/bin/python3
""" import tast_basemodel """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class Place_Test(test_basemodel):
    """ inherits from the test_basemodel class """

    def __init__(self, *args, **kwargs):
        """ overrides the __init__ method to set name and value """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def Test_City_id(self):
        """ Creates a new instance of the City class and checks that its city_id attribute is a string """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def Test_User_id(self):
        """ Creates a new instance of the City class and checks that its user_id attribute is a string"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def Test_Name(self):
        """ Creates a new instance of the City class and checks that its name attribute is a string """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def Test_description(self):
        """ Creates a new instance of the City class and checks that its description attribute is a string """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def Test_Rooms_Numbers(self):
        """ Creates a new instance of the City class and checks that its number_rooms attribute is a integer """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def Test_Bathrooms_Numbers(self):
        """ Creates a new instance of the City class and checks that its number_bathrooms attribute is a integer """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def Test_max_guest(self):
        """ Creates a new instance of the City class and checks that its max_guest attribute is a integer """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def Test_price_by_night(self):
        """ Creates a new instance of the City class and checks that its price_by_night attribute is a integer """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def Test_latitude(self):
        """ Creates a new instance of the City class and checks that its latitude attribute is a float """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def Test_longitude(self):
        """ Creates a new instance of the City class and checks that its longitude attribute is a float """
        new = self.value()
        self.assertEqual(type(new.longitude), float)

    def Test_amenity_ids(self):
        """ Creates a new instance of the City class and checks that its amenity_ids attribute is a list """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
