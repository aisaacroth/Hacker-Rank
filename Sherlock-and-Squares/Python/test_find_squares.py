#!/usr/bin/env python3
'''
Test Suite for the Find Squares Program

Author: Alexander Roth
Date:   2015-12-28
'''
from find_squares import find_square_roots
import unittest

class TestFindSquares(unittest.TestCase):

    def test_find_square_one(self):
        test_inputs = (3, 9)
        test_ans = find_square_roots(test_inputs[0], test_inputs[1])
        self.assertEqual(2, test_ans)

    def test_find_square_two(self):
        test_inputs = (17, 24)
        test_ans = find_square_roots(test_inputs[0], test_inputs[1])
        self.assertEqual(0, test_ans)



if __name__ == '__main__':
    unittest.main()
