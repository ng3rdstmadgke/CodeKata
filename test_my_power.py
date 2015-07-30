__author__ = 'midorikawakeita'

import unittest
import my_power

class my_power_1_TestCase(unittest.TestCase):
    def test_課題1(self):
        i=my_power.my_power_1(2,10)
        print(i)
        self.assertEqual(False, False)

    def test_課題2(self):
        i=my_power.my_power_1(2,10)
        print(i)
        self.assertEqual(False, False)

if __name__ == '__main__':
    unittest.main()
