#!/usr/bin/python3
"""Unittest model for the amenity class"""



import unittest
from datetime import datetime
import time
from models.amenity import amenity
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class testamenity(unittest.TestCase):
    """Test Cases for the amenity class"""

    def setup(self):
        """Sets up test methods"""
        pass

    def tearDown(self):
        """Tears down test methods"""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data"""
        FileStorage._FileStorage_objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage.FileStorage__file_path)

    def test_8_instantiation(self):
        """Tests instantiation of amenity class"""

        b = amenity()
        self.assertEqual(str(type(b)), "class 'models.amenity.amenity'>")
        self.assertIsInstance(b, amenity)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attriutes(self):
        """Test attributes of amenity class"""
        attributes = storage.attributes()["amenity"]
        o = amenity()
        for k,v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)


    if __name__ =="__main__":
                unittest.main()
