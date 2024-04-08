#!/usr/bin/env python3
""" Module containing unit test classes. """
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map
from utils import get_json


class TestAccessNestedMap(unittest.TestCase):
    """Test case class."""

    # 0. Parameterize a unit test
    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected_result):
        """Test method for utils.access_nested_map method."""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    # 1. Parameterize a unit test
    @parameterized.expand(
        [
            ({}, ("a",), "Key 'a' not found in nested map"),
            ({"a": 1}, ("a", "b"), "Key 'b' not found in nested map"),
        ]
    )
    def test_access_nested_map_exception(
        self, nested_map, path, expected_exception_msg
    ):
        """Test method for utils.test_access_nested_map"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
            self.assertEqual(str(context.exception), expected_exception_msg)


class TestGetJson(unittest.TestCase):
    """Test case class."""

    # 2. Mock HTTP calls
    @patch("utils.requests.get")
    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test method for utils.get_json"""
        mock_response = Mock()
        mock_response.json.response_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)
