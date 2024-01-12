#!/usr/bin/python3
from models.base_model import BaseModel
import unittest


class TestStringMethods(unittest.TestCase):

    def test_to_str(self):
        my_model = BaseModel()
        my_model.id = "azerty123456"
        self.assertIn(
            "[BaseModel] (azerty123456) {'id': 'azerty123456'", str(my_model))

    def test_to_dict(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        dictionary = my_model.to_dict()
        self.assertListEqual(list(dictionary.keys()), [
                             'id', 'created_at', 'updated_at', 'name', '__class__'])

    def test_save(self):
        my_model = BaseModel()
        first_date = my_model.updated_at
        my_model.save()
        second_date = my_model.updated_at
        self.assertNotEqual(first_date, second_date)


if __name__ == '__main__':
    unittest.main()
