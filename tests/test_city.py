#!/usr/bin/python3
"""
Test City class
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test suite for City class
    """

    def test_init(self):
        """
        Test initialization of City instance
        """
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_attributes(self):
        """
        Test setting attributes of City instance
        """
        city = City()
        city.state_id = "12345"
        city.name = "San Francisco"
        self.assertEqual(city.state_id, "12345")
        self.assertEqual(city.name, "San Francisco")
