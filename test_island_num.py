__author__ = 'midorikawakeita'

import unittest
import island_num


class MyTestCase(unittest.TestCase):
    def test_初期化メソッド(self):
        island_init=island_num.my_island("5 6 ##...##.#...#..###.....#.###..")
        print("行数(height)：{}".format(island_init.height))
        print("列数(width)：{}".format(island_init.width))
        print("入力文字列(map_str)：{}".format(island_init.map_str))
        print("入力内容で行列化(map_list)：{}".format(island_init.map_list))
        self.assertEqual(island_init.height , 5)
        self.assertEqual(island_init.width , 6)
        self.assertEqual(island_init.map_str , "##...##.#...#..###.....#.###..")
        self.assertEqual(island_init.map_list , [['#', '#', '.', '.', '.', '#'], ['#', '.', '#', '.', '.', '.'], ['#', '.', '.', '#', '#', '#'], ['.', '.', '.', '.', '.', '#'], ['.', '#', '#', '#', '.', '.']])

    def test_処理１(self):
        island_init=island_num.my_island("5 6 ##...##.#...#..###.....#.###..")
        my_rec=island_init.is_rec()
        print("置換後の行列：{}".format(my_rec))
        self.assertEqual(my_rec , [['+', '#', '.', '.', '.', '#'], ['#', '.', '#', '.', '.', '.'], ['#', '.', '.', '#', '#', '#'], ['.', '.', '.', '.', '.', '#'], ['.', '#', '#', '#', '.', '.']])



if __name__ == '__main__':
    unittest.main()
