__author__ = 'midorikawakeita'

import unittest
import my_batch

class MyTestCase(unittest.TestCase):
    def test_初期化メソッド(self):
        a = my_batch.Batch_form("N**ON*O*O*")
        a_a = a.b_list
        a_b = a.length
        a_c = a.forward
        a_d = a.backward
        print("b_list:{}  length:{}  forward:{}  backward:{}".format(a_a,a_b,a_c,a_d))

        b = my_batch.Batch_form("*ON***N*N")
        b_a = b.b_list
        b_b = b.length
        b_c = b.forward
        b_d = b.backward
        b_e = b.center
        print("b_list:{}  length:{}  forward:{}  backward:{}  center:{}".format(b_a,b_b,b_c,b_d,b_e))
        self.assertEqual(a_a, ['N', '*', '*', 'O', 'N', '*', 'O', '*', 'O', '*'])
        self.assertEqual(a_b, 10)
        self.assertEqual(a_c, ['N', '*', '*', 'O', 'N'])
        self.assertEqual(a_d, ['*', 'O', '*', 'O', '*'])

        self.assertEqual(b_a, ['*', 'O', 'N', '*', '*', '*', 'N', '*', 'N'])
        self.assertEqual(b_b, 9)
        self.assertEqual(b_c, ['*', 'O', 'N', '*'])
        self.assertEqual(b_d, ['*', 'N', '*', 'N'])
        self.assertEqual(b_e, ['*'])

    def test_回文を作成(self):
        a = my_batch.Batch_form("N**ON*O*O*")
        b = my_batch.Batch_form("*ON***N*N")
        c = my_batch.Batch_form("NONONONON")
        d = my_batch.Batch_form("NNONO*ONON")
        a1,a2 = a.make_batch()
        print(["".join(a1),a2])

        b1,b2 = b.make_batch()
        print(["".join(b1),b2])

        c1,c2 = c.make_batch()
        print(["".join(c1),c2])

        d1,d2 = d.make_batch()
        print(["".join(d1),d2])

        self.assertEqual(["".join(a1),a2], ['NONONNONON', 55])
        self.assertEqual(["".join(b1),b2], ['NONNNNNON', 55])
        self.assertEqual(["".join(c1),c2], ['NONONONON', 0])
        self.assertEqual(["".join(d1),d2], ['NNONO*ONON', -1])


if __name__ == '__main__':
    unittest.main()
