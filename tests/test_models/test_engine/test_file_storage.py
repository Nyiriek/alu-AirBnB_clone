#!/usr/bin/python3
""" Contains unittests for FileStorage class """
import unittest
import os
from models import storage
from models.base_model import BaseModel


class TestFileStorageClass(unittest.TestCase):
    """ Tests FileStorage class """

    def test_all(self):
        """ Tests all method """
        # create storage instance and instance of BaseModel

        obj = BaseModel()
        __objects = storage.all()
        # test that storage.all() returns dictionary
        self.assertIsI
