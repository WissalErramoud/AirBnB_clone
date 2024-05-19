#!/usr/bin/python3
"""
Test Review class
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test suite for Review class
    """

    def test_init(self):
        """
        Test initialization of Review instance
        """
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_attributes(self):
        """
        Test setting attributes of Review instance
        """
        review = Review()
        review.place_id = "12345"
        review.user_id = "67890"
        review.text = "Great place to stay!"
        self.assertEqual(review.place_id, "12345")
        self.assertEqual(review.user_id, "67890")
        self.assertEqual(review.text, "Great place to stay!")
