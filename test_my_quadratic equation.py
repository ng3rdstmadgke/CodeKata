__author__ = 'midorikawakeita'

import unittest
import my_quadratic_equation

class my_quadratic_equation_TestCase(unittest.TestCase):
    def test_my_quadratic_equation(self):
        i=my_quadratic_equation.quadratic_equation(0.0000000045,10,1)
        print(i)
        self.assertEqual(i, i)


if __name__ == '__main__':
    unittest.main()
