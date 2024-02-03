#!/usr/bin/env python3
""" A script to unit test for utils.access_nested_map
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ A class to test utils.access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])

    def test_access_nested_map(self, dict, path, expected):
        """Test the access of a nested map."""
        result = access_nested_map(dict, path)
        self.assertEqual(result, expected)