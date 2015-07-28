__author__ = 'midorikawakeita'

import unittest
import tenti_gyouretu


class tenti_gyouretu_TestCase(unittest.TestCase):
    def test_行列作成(self):
        l=tenti_gyouretu.make_gyo("1 2 3 4 5 6 7 8 9")
        print(l)
        self.assertEqual(False, False)

    def test_転置(self):
        n=tenti_gyouretu.tenti_gyo([['1', '2', '3','4'], ['5', '6','7', '8'], ['9','10','11','12'],['13','14','15','16']])
        print(n)
        self.assertEqual(False, False)

    def test_行列表示(self):
        tenti_gyouretu.print_gyo(['1', '5', '9', '13', '2', '6', '10', '14', '3', '7', '11', '15', '4', '8', '12', '16'])
        self.assertEqual(False, False)
if __name__ == '__main__':
    unittest.main()
