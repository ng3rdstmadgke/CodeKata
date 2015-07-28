__author__ = 'midorikawakeita'

import unittest
import my_calendar

class MyTestCase(unittest.TestCase):
    def test_２０００年５月(self):
        l=my_calendar.days(2000,5)
        self.assertEqual(l, 31)

    def test_２０００年2月(self):
        l=my_calendar.days(2000,2)
        self.assertEqual(l, 29)

    def test_２015年12月(self):
        l=my_calendar.days(2015,12)
        self.assertEqual(l, 31)

    def test_２015年12月(self):
        l=my_calendar.calendar_list(31,2)
        print(l)
        self.assertEqual(31, 31)


if __name__ == '__main__':
    unittest.main()
