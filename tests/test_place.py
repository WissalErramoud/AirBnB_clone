#!/usr/bin/python3
"""
Test Place class
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Test suite for Place class
    """

    def test_init(self):
        """
        Test initialization of Place instance
        """
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_attributes(self):
        """
        Test setting attributes of Place instance
        """
        place = Place()
        place.city_id = "12345"
        place.user_id = "67890"
        place.name = "Cozy Apartment"
        place.description = "A charming apartment in the heart of the city."
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 37.7749
        place.longitude = -122.4194
        place.amenity_ids = ["1", "2", "3"]
        self.assertEqual(place.city_id, "12345")
        self.assertEqual(place.user_id, "67890")
        self.assertEqual(place.name, "Cozy Apartment")
        self.assertEqual(place.description, "A charming apartment in"
                         " the heart of the city.")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ["1", "2", "3"])
