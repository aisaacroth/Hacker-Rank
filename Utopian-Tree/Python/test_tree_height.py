#/usr/bin/env python3
'''
Tester for Tree Height program.

Author: Alexander Roth
Date:   2015-12-28
'''
from tree_height import determine_tree_height
import unittest

class TestTreeHeight(unittest.TestCase):

    def test_tree_height_zero(self):
        test_input = 0
        test_ans = determine_tree_height(test_input)
        self.assertIsNotNone(test_ans)
        self.assertEqual(1, test_ans)

    def test_tree_height_one(self):
        test_input = 1
        test_ans = determine_tree_height(test_input)
        self.assertIsNotNone(test_ans)
        self.assertEqual(2, test_ans)

    def test_tree_height_two(self):
        test_input = 4
        test_ans = determine_tree_height(test_input)
        self.assertIsNotNone(test_ans)
        self.assertEqual(7, test_ans)


if __name__ == '__main__':
    unittest.main()
