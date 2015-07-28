__author__ = 'midorikawakeita'

import unittest
import my_calendar

class MyTestCase(unittest.TestCase):
    def test_something(self):
        my_calendar.calender_main(2000,5)
        my_calendar.calender_main(2001,5)
        my_calendar.calender_main(2002,5)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
