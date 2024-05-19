#!/usr/bin/python3
"""
Test User class
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test suite for User class
    """

    def test_init(self):
        """
        Test initialization of User instance
        """
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_attributes(self):
        """
        Test setting attributes of User instance
        """
        user = User()
        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
