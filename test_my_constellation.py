__author__ = 'midorikawakeita'

import unittest
import my_constellation

class My_constellation_TestCase(unittest.TestCase):
    def test_山羊座(self):
        t=my_constellation.constellation(12,25)
        print(t)
        self.assertEqual(t,"山羊座")

    def test_魚座(self):
        j=my_constellation.constellation(3,24)
        print(j)
        self.assertEqual(j,"牡羊座")


if __name__ == '__main__':
    unittest.main()
