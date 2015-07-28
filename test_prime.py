__author__ = 'midorikawakeita'

import unittest
import prime


class MyTestCase(unittest.TestCase):
    def test_１の時(self):
        p=prime.prime(1)
        self.assertEqual(p,False)

    def test_０の時(self):
        p=prime.prime(0)
        self.assertEqual(p,False)

    def test_０以下の時(self):
        p=prime.prime(-1)
        self.assertEqual(p,False)

    def test_素数の時(self):
        p=prime.prime(3)
        self.assertEqual(p,True)

    def test_素数じゃない時(self):
        p=prime.prime(4)
        self.assertEqual(p,False)


if __name__ == '__main__':
    unittest.main()
