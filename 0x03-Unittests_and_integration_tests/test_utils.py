#!/usr/bin/env python3
""" A script to unit test for utils.access_nested_map
"""

import unittest
from unittest import mock
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """ A class to test utils.access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),

        ])

    def test_access_nested_map(self, dict, path, expected):
        """Test the access of a nested map."""
        result = access_nested_map(dict, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), KeyError, 'a'),
        ({"a": 1}, ("a", "b"), KeyError, 'b')
    ])
    def test_access_nested_map_exception(self, dict, path, expected, expected_key):
        with self.assertRaises(expected):
            access_nested_map(dict, path)

    class TestGetJson(unittest.TestCase):
        """ mock requests"""

        @parameterized.expand([
            {"test_url": "http://example.com", "test_payload": {"payload": True}},
            {"test_url": "http://holberton.io", "test_payload": {"payload": False}}
        ])

        @mock.patch('utils.get_json')
        def test_get_json(self, url, mock_get_json, expected):
            """ test that utils.get_json returns the expected result. """
            mock_get_json.return_value.json.return_value = expected
            mock_get_json.assertcalledOnceWith(url)
            result = get_json(url)
            self.assertEqual(result, expected)
