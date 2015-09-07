__author__ = 'midorikawakeita'

import unittest
import island_num


class MyTestCase(unittest.TestCase):
    def test_初期化メソッド(self):
        island_init=island_num.my_island("5 6 .#...####...#.####.....#.###..")
        print("行数(height)：{}".format(island_init.height))
        print("列数(width)：{}".format(island_init.width))
        print("入力文字列(map_str)：{}".format(island_init.map_str))
        print("入力内容で行列化(map_list)：{}".format(island_init.map_list))
        self.assertEqual(island_init.height , 5)
        self.assertEqual(island_init.width , 6)
        self.assertEqual(island_init.map_str , ".#...####...#.####.....#.###..")
        self.assertEqual(island_init.map_list , [['.', '#', '.', '.', '.', '#'], ['#', '#', '#', '.', '.', '.'], ['#', '.', '#', '#', '#', '#'], ['.', '.', '.', '.', '.', '#'], ['.', '#', '#', '#', '.', '.']])

    def test_処理１(self):
        island_init=island_num.my_island("5 6 .#...####...#.####.....#.###..")
        my_rec=island_init.is_rec([['.', '#', '.', '.', '.', '#'], ['#', '#', '#', '.', '.', '.'], ['#', '.', '#', '#', '#', '#'], ['.', '.', '.', '.', '.', '#'], ['.', '#', '#', '#', '.', '.']])
        print("置換後の行列：{}".format(my_rec))
        self.assertEqual(my_rec , [['.', '+', '.', '.', '.', '#'], ['#', '#', '#', '.', '.', '.'], ['#', '.', '#', '#', '#', '#'], ['.', '.', '.', '.', '.', '#'], ['.', '#', '#', '#', '.', '.']])

    def test_処理１_全部海の場合(self):
        island_init=island_num.my_island("5 6 ..............................")
        my_rec=island_init.is_rec([['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.']])
        print("すべて海の時：{}".format(my_rec))
        self.assertEqual(my_rec , 1)

    def test_処理2(self):
        island_init=island_num.my_island("5 6 .#...####...#.####.....#.###..")
        my_left = island_init.left([['.', '+', '.', '.', '.', '#'], ['#', '#', '#', '.', '.', '.'], ['#', '.', '#', '#', '#', '#'], ['.', '.', '.', '.', '.', '#'], ['.', '#', '#', '#', '.', '.']])
        print("下と右側を＋に変換：{}".format(my_left))
        self.assertEqual(my_left , [['.', '+', '.', '.', '.', '#'], ['+', '+', '+', '.', '.', '.'], ['+', '.', '+', '+', '+', '+'], ['.', '.', '.', '.', '.', '+'], ['.', '#', '#', '#', '.', '.']])

    def test_処理3(self):
        island_init=island_num.my_island("5 6 .#...####...#.####.....#.###..")
        my_del=island_init.is_del([['.', '+', '.', '.', '.', '#'], ['+', '+', '+', '.', '.', '.'], ['+', '.', '+', '+', '+', '+'], ['.', '.', '.', '.', '.', '+'], ['.', '#', '#', '#', '.', '.']])
        print("+を.にする：{}".format(my_del))
        self.assertEqual(my_del , [['.', '.', '.', '.', '.', '#'], ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['.', '#', '#', '#', '.', '.']])

    def test_main1(self):
        island_init=island_num.my_island("5 6 .#...####...#.####.....#.###..")
        my_main=island_init.main()
        print("島の数：{}".format(my_main))
        self.assertEqual(my_main , 3)

    def test_main2(self):
        island_init=island_num.my_island("10 10 .#...####...#.####...###.#...........##..#...####.###..##.#.#.#..##.#.#.##.##.#..#.........#...####.")
        my_main=island_init.main()
        print("島の数：{}".format(my_main))
        self.assertEqual(my_main , 7)

if __name__ == '__main__':
    unittest.main()
