__author__ = 'midorikawakeita'
# -*- coding: utf-8 -*-

import unittest
import fizzbuzz

class MyTestCase(unittest.TestCase):
    def test_引数3(self):
        string_data = fizzbuzz.fizzbuzz(3)
        self.assertEqual(string_data, "Fizz")

    def test_引数5(self):
        string_data = fizzbuzz.fizzbuzz(5)
        self.assertEqual(string_data, "Buzz")

    def test_引数15(self):
        string_data = fizzbuzz.fizzbuzz(15)
        self.assertEqual(string_data, "FizzBuzz")


if __name__ == '__main__':
    unittest.main()
