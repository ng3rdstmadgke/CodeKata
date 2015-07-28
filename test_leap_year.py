__author__ = 'midorikawakeita'

import unittest
import leap_year

class leap_year_TestCase(unittest.TestCase):
    def test_4の倍数(self):
        leap_year.leap_year(2016)
        self.assertEqual(True,True)

    def test_100の倍数(self):
        leap_year.leap_year(1900)
        self.assertEqual(False,False)

    def test_400の倍数(self):
        leap_year.leap_year(2000)
        self.assertEqual(True,True)


if __name__ == '__main__':
    unittest.main()
