#!/usr/bin/env python3
""" Module containing unit tests. """
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNesteMap(unittest.TestCase):
    """Test case class. """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """ test method for utils.access_nested_map method. """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)
