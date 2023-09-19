#!/usr/bin/python3
import unittest
from models import Amenity
import datetime


class TestAmenity(unittest.TestCase):
    def setUp(self):
    
        self.test_model1 = Amenity()
        self.test_model2 = Amenity()

    def test_basic_setup(self):

        self.assertTrue(hasattr(self.test_model1, "name"))
        self.assertTrue(self.test_model1.id != self.test_model2.id)
        m1c = self.test_model1.created_at
        m2c = self.test_model2.created_at
        self.assertTrue(m1c != m2c)
