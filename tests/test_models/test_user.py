#!/usr/bin/python3
"""Unittest module for User."""

import os
import models
import unittest
from models.user import User
from models.engine.file_storage import FileStorage


class Test_User(unittest.TestCase):
    """Class for User test cases."""

    def setUp(self):
        """Set up tests."""
        storage.reset()

    def test_check_user(self):
        """Test to check a user."""
        self.assertEqual(User().__class__.__name__, "User")

    def test_to_dict(self):
        """Tests to dictionary."""
        self.assertTrue(dict, type(User().to_dict()))

    def st_save(self):
        """Tests for save."""
        with self.assertRaises(TypeError):
            User().save(None)

    def test_is_an_instance(self):
        """Tests an instance of BaseModel."""
        self.assertIsInstance(User(), User)

    def test_types(self):
        """Test for types."""
        self.assertEqual(type(User().id), str)
        self.assertEqual(type(User().email), str)
        self.assertEqual(type(User().password), str)
        self.assertEqual(type(User().first_name), str)
        self.assertEqual(type(User().last_name), str)
        self.assertEqual(User().created_at.__class__.__name__, "datetime")
        self.assertEqual(User().updated_at.__class__.__name__, "datetime")

    def test_executable(self):
        """tests for executable permissions."""
        is_read_true = os.access('models/engine/file_storage.py', os.R_OK)
        self.assertTrue(is_read_true)
        is_write_true = os.access('models/engine/file_storage.py', os.W_OK)
        self.assertTrue(is_write_true)
        is_exec_true = os.access('models/engine/file_storage.py', os.X_OK)
        self.assertTrue(is_exec_true)


if __name__ == '__main__':
    unittest.main()
