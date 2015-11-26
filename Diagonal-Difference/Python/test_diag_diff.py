#!/usr/bin/env python3
''' Tester for the Diagonal Difference program.

Author: Alexander Roth
Date:   2015-11-26
'''
from diag_diff import diag_sum
import unittest

class TestDiagonalDifference(unittest.TestCase):

    def test_diag_sum(self):
        test_input = [[11, 2, 4],[4, 5, 6], [10, 8, -12]]
        test_ans = diag_sum(test_input)
        self.assertIsNotNone(test_ans)
        self.assertEqual(15, test_ans)


if __name__ == '__main__':
    unittest.main()
