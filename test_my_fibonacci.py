__author__ = 'midorikawakeita'

import unittest
import my_fibonacci

class my_fibonacci_TestCase(unittest.TestCase):
    def test_再起処理なし_第5項(self):
        n=my_fibonacci.make_fibonacci_2(5)
        print(n)
        self.assertEqual(n,n)

    def test_再起処理なし_第10項(self):
        n=my_fibonacci.make_fibonacci_2(10)
        print(n)
        self.assertEqual(n,n)

    def test_再起処理なし_第100項(self):
        n=my_fibonacci.make_fibonacci_2(20)
        print(n)
        self.assertEqual(n,n)

    def test_再起処理あり_第5項(self):
        n=my_fibonacci.make_fibonacci_1(5,1,1)
        print(n)
        self.assertEqual(n,n)


if __name__ == '__main__':
    unittest.main()
