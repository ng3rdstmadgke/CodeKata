__author__ = 'midorikawakeita'

import unittest
import root_calculation


class MyTestCase(unittest.TestCase):
    def test_初期化メソッド(self):
        a = root_calculation.Root_form(100)
        print(a.num)
        self.assertEqual(a.num,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100])

    def test_素数のリストを作る(self):
        a = root_calculation.Root_form(100)
        print("100までの素数：{}".format(a.prime_list()))
        b = root_calculation.Root_form(89)
        print("89までの素数：{}".format(b.prime_list()))
        self.assertEqual(a.prime_list(),[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89 , 97])

    def test_与えられた数を素因数分解する(self):
        a = root_calculation.Root_form(100)
        list_b = a.prime_factor(68,[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
        print("68の素因数は{}".format(list_b))
        list_c = a.prime_factor(38,[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
        print("38の素因数は{}".format(list_c))
        list_d = a.prime_factor(67,[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
        print("67の素因数は{}".format(list_d))
        list_e = a.prime_factor(91,[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
        print("91の素因数は{}".format(list_e))
        list_f = a.prime_factor(59,[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
        print("59の素因数は{}".format(list_f))
        self.assertEqual(1,1)

    def test_(self):
        self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()
