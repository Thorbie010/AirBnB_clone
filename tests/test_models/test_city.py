#!/usr/bin/python3
"""Unittest module for File storage"""

import os
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import City


class Test_City(unittest.TestCase):
    """A class for File city test cases."""

    def setUp(self):
        """Set up tests."""
        storage.reset()


