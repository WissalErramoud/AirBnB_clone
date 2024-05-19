#!/usr/bin/python3
"""
Test BaseModel class
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test suite for BaseModel class
    """

    def test_init(self):
        """
        Test initialization of BaseModel instance
        """
        base_model = BaseModel()
        self.assertIsNotNone(base_model.id)
        self.assertIsNotNone(base_model.created_at)
        self.assertIsNotNone(base_model.updated_at)

    def test_save(self):
        """
        Test the save method
        """
        base_model = BaseModel()
        old_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(old_updated_at, base_model.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method
        """
        base_model = BaseModel()
        base_model.name = "Test Model"
        base_model.number = 123
        base_model_dict = base_model.to_dict()
        self.assertEqual(base_model_dict["__class__"], "BaseModel")
        self.assertEqual(base_model_dict["name"], "Test Model")
        self.assertEqual(base_model_dict["number"], 123)
        self.assertEqual(base_model_dict["id"], base_model.id)
        self.assertEqual(base_model_dict["created_at"],
                         base_model.created_at.isoformat())
        self.assertEqual(base_model_dict["updated_at"],
                         base_model.updated_at.isoformat())

    def test_str(self):
        """
        Test the __str__ method
        """
        base_model = BaseModel()
        base_model.name = "Test Model"
        base_model.number = 123
        expected_str = "[BaseModel] ({}) {}".format(
            base_model.id, base_model.__dict__)
        self.assertEqual(str(base_model), expected_str)

    def test_init_with_kwargs(self):
        """
        Test initialization with keyword arguments
        """
        base_model = BaseModel(
            id="1234",
            created_at="2023-10-27T12:34:56.789012",
            updated_at="2023-10-27T12:34:56.789012",
            name="Test Model"
        )
        self.assertEqual(base_model.id, "1234")
        self.assertEqual(base_model.name, "Test Model")
        self.assertEqual(base_model.created_at.isoformat(),
                         "2023-10-27T12:34:56.789012")
        self.assertEqual(base_model.updated_at.isoformat(),
                         "2023-10-27T12:34:56.789012")
