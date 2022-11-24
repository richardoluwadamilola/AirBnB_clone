#!/usr/bin/python3
"""
Unittest for state.py
"""
import unittest
from models.state import State
from datetime import datetime

class TestState(unittest.TestCase):
    #Test instances and methods from State class

    s = State()

    def test_class_exists(self):
        #test if class exists
        res = "<class 'models.state.State'>"
        self.assertEqual(str(type.s)), res)

    def test_user_inheritance(self):
        #test if state is a subclass of base class/model
        self.assertInInstance(self.s, State)

    def testHasAttributes(self):
        #verify if attributes exist
        self.assertTrue(hasattr(self.s, 'name'))
        self.assertTrue(hasattr(self.s, 'id'))
        self.assertTrue(hasattr(self.s, 'created_at'))
        self.assertTrue(hasattr(self.s, 'updated_at'))

    def test_types(self):
        #tests if the type of the attribute is the correct one
        self.assertIsInstance(self.s.name, str)
        self.assertIsInstance(self.s.id, str)
        self.assertIsInstance(self.s.created_at, datetime.datetime)
        self.assertIsInstance(self.s.updated_at, datetime.datetime)

if __name__ == '__main__':
        unittest.main()
