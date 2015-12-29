#!/usr/bin/env python3
'''
Test Suite for Find Digits program.

Author: Alexander Roth
Date:   2015-12-28
'''
from find_digits import find_divisible_digits, get_digits
import unittest

class TestFindDigits(unittest.TestCase):

    def test_get_digits_12(self):
        test_input = 12
        test_ans = get_digits(test_input)
        self.assertIsNotNone(test_ans)
        self.assertEqual([1, 2], test_ans)

    def test_get_digits_1012(self):
        test_input = 1012
        test_ans = get_digits(test_input)
        self.assertIsNotNone(test_ans)
        self.assertEqual([1, 0, 1, 2], test_ans)

    def test_find_divisible_one(self):
        test_input = 12
        test_ans = find_divisible_digits(test_input)
        self.assertIsNotNone(test_ans)
        self.assertEqual(2, test_ans)

    def test_find_divisible_two(self):
        test_input = 1012
        test_ans = find_divisible_digits(test_input)
        self.assertIsNotNone(test_ans)
        self.assertEqual(3, test_ans)


if __name__ == '__main__':
    unittest.main()
