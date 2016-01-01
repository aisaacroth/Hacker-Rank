#!/usr/bin/env python3
'''
Test suite for Caesar Cipher program.

Author: Alexander Roth
Date:   2016-01-01
'''
from caesar_cipher import encode
import unittest

class TestCaesarCipher(unittest.TestCase):

    def test_encode(self):
        test_input = 'alex'
        test_ans = encode(test_input, 0)
        self.assertIsNotNone(test_ans)
        self.assertEqual(test_input, test_ans)

    def test_encode_two(self):
        test_input = 'middle-Outz'
        test_ans = encode(test_input, 2)
        self.assertIsNotNone(test_ans)
        self.assertEqual('okffng-Qwvb', test_ans)


if __name__ == '__main__':
    unittest.main()
