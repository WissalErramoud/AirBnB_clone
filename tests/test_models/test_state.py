#!/usr/bin/python3
"""
Test State class
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    Test suite for State class
    """

    def test_init(self):
        """
        Test initialization of State instance
        """
        state = State()
        self.assertEqual(state.name, "")

    def test_attributes(self):
        """
        Test setting attributes of State instance
        """
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")
