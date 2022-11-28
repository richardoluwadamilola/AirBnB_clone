#!/usr/bin/python3
"""
Unittests for user.py
"""

import unittest
from models.user import User
from datetime import datetime


class UserCase(unittest.TestCase):
    """Test instances and methods from user class"""

    person = User()

    def test_class_exists(self):
        """test if class exist"""
        self.assertEqual(str(type(self.person)), "<class 'models.user.User'>")

    def test_user_inheritance(self):
        """test if the user class is a subclass of the base class/model"""
        self.assertIsInstance(self.person, User)

    def testHasAttributes(self):
        """verify if attributes exists"""
        self.assertTrue(hasattr(self.person, 'email'))
        self.assertTrue(hasattr(self.person, 'password'))
        self.assertTrue(hasattr(self.person, 'first_name'))
        self.assertTrue(hasattr(self.person, 'last_name'))
        self.assertTrue(hasattr(self.person, 'id'))
        self.assertTrue(hasattr(self.person, 'created_at'))
        self.assertTrue(hasattr(self.person, 'updated_at'))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.person.first_name, str)
        self.assertIsInstance(self.person.last_name, str)
        self.assertIsInstance(self.person.email, str)
        self.assertIsInstance(self.person.password, str)
        self.assertIsInstance(self.person.id, str)
        self.assertIsInstance(self.person.created_at, datetime.datetime)
        self.assertIsInstance(self.person.updated_at, datetime.datetime)


if __name__ == '__main__':
        unittest.main()
