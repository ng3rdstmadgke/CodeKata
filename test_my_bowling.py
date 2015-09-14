__author__ = 'midorikawakeita'

import unittest
import my_bowling

class MyTestCase(unittest.TestCase):
    def test_初期化メソッド(self):
        a = my_bowling.My_Bowling("19 6 2 0 3 5 5 0 8 10 1 9 3 6 6 4 10 5 5 3")
        b = a.throw
        c = a.raw_score
        d = a.ps_score
        print(b)
        print(c)
        print(d)
        aa = my_bowling.My_Bowling("20 1 9 2 8 3 7 4 6 10 0 0 6 4 7 3 8 2 7 1")
        bb = aa.ps_score
        print(bb)
        aaa = my_bowling.My_Bowling("12 10 10 10 10 10 10 10 10 10 10 10 10")
        bbb = aaa.ps_score
        print(bbb)
        self.assertEqual(True, True)

    def test_ノーマル(self):
        a = my_bowling.My_Bowling("12 10 10 10 10 10 10 10 10 10 10 10 10")
        b = a.normal_score([6, 2], [0, 3], [5, 5])
        c = a.normal_score([10, 0], [10, 0], [10, 0])
        d = a.normal_score([10, 0], [0, 0], [6, 4])
        e = a.normal_score([10, 0], [10, 0], [7, 3])
        print(b)
        print(c)
        print(d)
        print(e)
        print("")
        self.assertEqual(True, True)


    def test_ナイン(self):
        a = my_bowling.My_Bowling("12 10 10 10 10 10 10 10 10 10 10 10 10")
        b = a.nine_score([10, 0], [10, 3, 2])
        c = a.nine_score([10, 0], [5, 5, 3])
        d = a.nine_score([8, 2], [7, 1, 0])
        e = a.nine_score([10, 0], [10, 10, 10])
        print(b)
        print(c)
        print(d)
        print(e)
        print("")
        self.assertEqual(True, True)

    def test_メイン１(self):
        a = my_bowling.My_Bowling("12 10 10 10 10 10 10 10 10 10 10 10 10")
        b = a.main_1()
        print(b)

        aa = my_bowling.My_Bowling("19 6 2 0 3 5 5 0 8 10 1 9 3 6 6 4 10 5 5 3")
        bb = aa.main_1()
        print(bb)

        aaa = my_bowling.My_Bowling("21 1 9 1 9 1 9 1 0 1 9 1 9 1 9 0 1 1 9 1 9 4")
        bbb = aaa.main_1()
        print(bbb)

        aaaa = my_bowling.My_Bowling("20 1 9 2 8 3 7 4 6 10 0 0 6 4 7 3 8 2 9 1 2")
        bbbb = aaaa.main_1()
        print(bbbb)

        aaaaa = my_bowling.My_Bowling("20 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0")
        bbbbb = aaaaa.main_1()
        print(bbbbb)
        print("")

    def test_メイン2(self):
        a = my_bowling.My_Bowling("12 10 10 10 10 10 10 10 10 10 10 10 10")
        b = a.main_2()
        print(b)

        aa = my_bowling.My_Bowling("19 6 2 0 3 5 5 0 8 10 1 9 3 6 6 4 10 5 5 3")
        bb = aa.main_2()
        print(bb)

        aaa = my_bowling.My_Bowling("21 1 9 1 9 1 9 1 0 1 9 1 9 1 9 0 1 1 9 1 9 4")
        bbb = aaa.main_2()
        print(bbb)

        aaaa = my_bowling.My_Bowling("20 1 9 2 8 3 7 4 6 10 0 0 6 4 7 3 8 2 9 1 2")
        bbbb = aaaa.main_2()
        print(bbbb)

        aaaaa = my_bowling.My_Bowling("20 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0")
        bbbbb = aaaaa.main_2()
        print(bbbbb)
        print("")



if __name__ == '__main__':
    unittest.main()
