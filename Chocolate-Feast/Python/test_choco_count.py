#!/usr/bin/env python3
'''
Test suite for the Chocolate Count program.

Author: Alexander Roth
Date:   2015-12-31
'''

from choco_count import count_chocolate
import unittest

class TestChocolateCount(unittest.TestCase):

    def test_choco_count_one(self):
        test_input = (10, 2, 5)
        test_ans = count_chocolate(test_input[0], test_input[1], test_input[2])
        self.assertIsNotNone(test_ans)
        self.assertEqual(6, test_ans)

    def test_choco_count_two(self):
        test_input = (12, 4, 4)
        test_ans = count_chocolate(test_input[0], test_input[1], test_input[2])
        self.assertIsNotNone(test_ans)
        self.assertEqual(3, test_ans)

    def test_choco_count_three(self):
        test_input = (6, 2, 2)
        test_ans = count_chocolate(test_input[0], test_input[1], test_input[2])
        self.assertIsNotNone(test_ans)
        self.assertEqual(5, test_ans)


if __name__ == '__main__':
    unittest.main()
