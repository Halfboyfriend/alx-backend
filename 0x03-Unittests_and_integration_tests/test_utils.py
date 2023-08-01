#!/usr/bin/env python3
"""
Parameterize a unit test
"""
import unittest
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import (access_nested_map, get_json, memoize)



class TestAccessNestedMap(unittest.TestCase):
    """Tests for access_nested_map Functions"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Dict, 
                            path: Tuple[str], 
                            expected_result: Union[Dict, int]) -> None:
        """Test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])

    def test_access_nested_map_exception(self, 
            nested_map: Dict, path, 
            exception: Exception) -> None:
        """Testing for exceptions"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)
