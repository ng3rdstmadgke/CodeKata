__author__ = 'midorikawakeita'

import unittest
import root_rationalization


class MyTestCase(unittest.TestCase):
    def test_100までの素数リスト_初期化メソッド(self):
        a = root_rationalization.Rationalization()
        b = a.prime_list
        print("\n--1--")
        print("100までの素数リスト：{}".format(b))
        self.assertEqual(b, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
                             97])

    def test_素因数リストを作成(self):
        a = root_rationalization.Rationalization()
        b = a.prime_factor(60)
        c = a.prime_factor(48)
        print("\n--2--")
        print("60の素因数リスト：{}".format(b))
        print("48の素因数リスト：{}".format(c))
        self.assertEqual(b, [2, 2, 3, 5])
        self.assertEqual(c, [2, 2, 2, 2, 3])

    def test_素因数個数リスト(self):
        a = root_rationalization.Rationalization()
        b = a.prime_and_number([2, 2, 3, 5])
        c = a.prime_and_number([2, 2, 2, 2, 3])
        print("\n--3--")
        print("60の素因数・個数リスト：{}".format(b))
        print("48の素因数・個数リスト：{}".format(c))
        self.assertEqual(b, [[2, 2], [3, 1], [5, 1]])
        self.assertEqual(c, [[2, 4], [3, 1]])

    def test_ルート内数字リスト(self):
        a = root_rationalization.Rationalization()
        b = a.root_num([[2, 2], [3, 1], [5, 1]])
        c = a.root_num([[2, 4], [3, 1]])
        print("\n--4--")
        print("60のルート内数字リスト：{}".format(b))
        print("48のルート内数字リスト：{}".format(c))
        self.assertEqual(b, [3, 5])
        self.assertEqual(c, [3])

    def test_要素数が奇数の数字の要素数に1足す(self):
        a = root_rationalization.Rationalization()
        b = a.num_plus([[2, 2], [3, 1], [5, 1]])
        c = a.num_plus([[2, 4], [3, 1]])
        print("\n--5--")
        print("60のリストに１足す：{}".format(b))
        print("48のリストに１足す：{}".format(c))
        self.assertEqual(b, [[2, 2], [3, 2], [5, 2]])
        self.assertEqual(c, [[2, 4], [3, 2]])

    def test_ルートをわかりやすく計算(self):
        a = root_rationalization.Rationalization()
        b = a.root_result([[2, 2], [3, 1], [5, 1]])
        c = a.root_result([[2, 4], [3, 2]])
        print("\n--6--")
        print("60をわかりやすく計算：{}".format(b))
        print("48をわかりやすく計算：{}".format(c))
        self.assertEqual(b, [2, 15])
        self.assertEqual(c, [12, 1])

    def test_最大公約数で割る(self):
        a = root_rationalization.Rationalization()
        b = a.reduction(2, 12)
        c = a.reduction(60, 48)
        print("\n--7--")
        print("2と12を最大公約数で割った数：{}".format(b))
        print("60と48を最大公約数で割った数：{}".format(c))
        self.assertEqual(b, [1, 6])
        self.assertEqual(c, [5, 4])

    def test_有理化(self):
        a = root_rationalization.Rationalization()
        b,bb,c,cc = a.main_act(2, 12)
        d,dd,e,ee = a.main_act(60, 48)
        print("\n--8--")
        print("2/12を有理化：{} {} {} {}".format(b,bb,c,cc))
        print("60/48を有理化：{} {} {} {}".format(d,dd,e,ee))
        list1=[b,bb,c,cc]
        list2=[d,dd,e,ee]
        self.assertEqual(list1,[1,6,6,1])
        self.assertEqual(list2,[1,5,2,1])


if __name__ == '__main__':
    unittest.main()
