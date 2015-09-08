__author__ = 'midorikawakeita'

import unittest
import critical_path

class MyTestCase(unittest.TestCase):
    def test_初期化(self):
        c_init = critical_path.Critical("7 9 A B 10 A C 3 B D 4 B E 7 C D 7 C F 9 D E 2 E G 1 F G 7")
        print("node:{}  type:{}".format(c_init.node,type(c_init.node)))
        print("path:{}  type:{}".format(c_init.path,type(c_init.path)))
        print("list:{}".format(c_init.list))
        print("map:{}".format(c_init.c_map))
        self.assertEqual(c_init.node, 7)
        self.assertEqual(c_init.path, 9)
        self.assertEqual(c_init.list, [[0, 1, 10], [0, 2, 3], [1, 3, 4], [1, 4, 7], [2, 3, 7], [2, 5, 9], [3, 4, 2], [4, 6, 1], [5, 6, 7]])
        self.assertEqual(c_init.c_map, [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])

    def test_英数変換(self):
        c_init = critical_path.Critical("7 9 A B 10 A C 3 B D 4 B E 7 C D 7 C F 9 D E 2 E G 1 F G 7")
        print("A:{}  B:{}  C:{}  D:{}  E:{}  F:{}  G:{}".format(c_init.si_convert("A"),c_init.si_convert("B"),c_init.si_convert("C"),c_init.si_convert("D"),c_init.si_convert("E"),c_init.si_convert("F"),c_init.si_convert("G")))
        print("0:{}  1:{}  2:{}  3:{}  4:{}  5:{}  6:{}".format(c_init.si_convert(0),c_init.si_convert(1),c_init.si_convert(2),c_init.si_convert(3),c_init.si_convert(4),c_init.si_convert(5),c_init.si_convert(6)))
        self.assertEqual(c_init.si_convert("A"), 0)
        self.assertEqual(c_init.si_convert("B"), 1)
        self.assertEqual(c_init.si_convert("C"), 2)
        self.assertEqual(c_init.si_convert(0), "A")
        self.assertEqual(c_init.si_convert(1), "B")
        self.assertEqual(c_init.si_convert(2), "C")

    def test_cost記入済みマップを返す(self):
        c_init = critical_path.Critical("7 9 A B 10 A C 3 B D 4 B E 7 C D 7 C F 9 D E 2 E G 1 F G 7")
        print(c_init.map_edit())
        self.assertEqual(c_init.map_edit(),[[0, 10, 3, 0, 0, 0, 0], [0, 0, 0, 14, 17, 0, 0], [0, 0, 0, 10, 0, 12, 0], [0, 0, 0, 0, 16, 0, 0], [0, 0, 0, 0, 0, 0, 18], [0, 0, 0, 0, 0, 0, 19], [0, 0, 0, 0, 0, 0, 0]])

    def test_クリティカルパスのコスト(self):
        c_init = critical_path.Critical("7 9 A B 10 A C 3 B D 4 B E 7 C D 7 C F 9 D E 2 E G 1 F G 7")
        a=c_init.max_cost([[0, 10, 3, 0, 0, 0, 0], [0, 0, 0, 14, 17, 0, 0], [0, 0, 0, 10, 0, 12, 0], [0, 0, 0, 0, 16, 0, 0], [0, 0, 0, 0, 0, 0, 18], [0, 0, 0, 0, 0, 0, 19], [0, 0, 0, 0, 0, 0, 0]])
        print(a)
        self.assertEqual(a,19)

    def test_クリティカルパスのコスト(self):
        c_init = critical_path.Critical("7 9 A B 10 A C 3 B D 4 B E 7 C D 7 C F 9 D E 2 E G 1 F G 7")
        a=c_init.critical_list([[0, 10, 3, 0, 0, 0, 0], [0, 0, 0, 14, 17, 0, 0], [0, 0, 0, 10, 0, 12, 0], [0, 0, 0, 0, 16, 0, 0], [0, 0, 0, 0, 0, 0, 18], [0, 0, 0, 0, 0, 0, 19], [0, 0, 0, 0, 0, 0, 0]])
        print(a)
        self.assertEqual(a,['A', 'C', 'F', 'G'])


if __name__ == '__main__':
    unittest.main()
