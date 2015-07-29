__author__ = 'midorikawakeita'

import unittest
import my_base64

class my_base64_TestCase(unittest.TestCase):
    def test_バリューリスト(self):
        d=my_base64.base64_dict()
        print(d)
        self.assertEqual(False, False)

    def test_2進数テキスト(self):
        i=my_base64.convert_text("abcdefghijklmn")
        print(i)
        self.assertEqual(False, False)

    def test_コードに変換(self):
        n=my_base64.code_base64(i,d)
        print(n)
        self.assertEqual(False, False)

if __name__ == '__main__':
    unittest.main()
