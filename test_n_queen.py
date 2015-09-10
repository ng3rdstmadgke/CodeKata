__author__ = 'midorikawakeita'

import unittest
import n_queen


class MyTestCase(unittest.TestCase):
    def test_初期化メソッド(self):
        a = n_queen.N_queen("....... ....... ..Q.... ....... ...Q... ....... .......")
        b = a.base_map
        c = a.height
        d = a.width
        print(b)
        print(c,d)
        self.assertEqual(b,[['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', 'Q', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', 'Q', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.']])
        self.assertEqual(c,7)
        self.assertEqual(d,7)

    def test_Ｑを探す(self):
        a = n_queen.N_queen("....... ....... ..Q.... ....... ...Q... ....... .......")
        b,c = a.search_q()
        print(""b,c)

        self.assertEqual(1,1)

    def test_something(self):
        self.assertEqual(1,1)


if __name__ == '__main__':
    unittest.main()
