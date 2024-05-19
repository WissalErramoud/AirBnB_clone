#!/usr/bin/python3
"""
Test Amenity class
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test suite for Amenity class
    """

    def test_init(self):
        """
        Test initialization of Amenity instance
        """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_attributes(self):
        """
        Test setting attributes of Amenity instance
        """
        amenity = Amenity()
        amenity.name = "WiFi"
        self.assertEqual(amenity.name, "WiFi")
