#/usr/bin/env python3
'''
Tester for Decent Number program.

Author: Alexander Roth
Date:   2015-12-28
'''
from decent_number import generate_decent_number, get_pivot
import unittest

class TestDecentNumber(unittest.TestCase):

    def test_get_pivot_negative(self):
        test_input = 1
        test_ans = get_pivot(test_input)
        self.assertIsNotNone(test_ans)
        self.assertEqual(-4, test_ans)

    def test_get_pivot_3(self):
        test_input = 3
        test_ans = get_pivot(test_input)
        self.assertIsNotNone(test_ans)
        self.assertEqual(3, test_ans)

    def test_get_pivot_5(self):
        test_input = 5
        test_ans = get_pivot(test_input)
        self.assertIsNotNone(test_ans)
        self.assertEqual(0, test_ans)

    def test_get_pivot_11(self):
        test_input = 11
        test_ans = get_pivot(test_input)
        self.assertIsNotNone(test_ans)
        self.assertEqual(6, test_ans)

    def test_gen_decent_number_bad(self):
        test_input = 1
        test_ans = generate_decent_number(test_input)
        self.assertIsNotNone(test_ans)
        self.assertEqual(-1, test_ans)

    def test_gen_decent_number_3(self):
        test_input = 3
        test_ans = generate_decent_number(test_input)
        self.assertIsNotNone(test_ans)
        self.assertEqual(555, test_ans)

    def test_gen_decent_number_3(self):
        test_input = 5
        test_ans = generate_decent_number(test_input)
        self.assertIsNotNone(test_ans)
        self.assertEqual(33333, test_ans)

    def test_gen_decent_number_11(self):
        test_input = 11
        test_ans = generate_decent_number(test_input)
        self.assertIsNotNone(test_ans)
        self.assertEqual(55555533333, test_ans)


if __name__ == '__main__':
    unittest.main()
