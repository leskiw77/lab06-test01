import unittest

from eternal.main import calculate, main

"""
Run with PYTHONPATH=. python tests/test_dummy.py
"""


class TestDummy(unittest.TestCase):

    def test_fun(self):
        weekday = calculate(2001, 1, 3)
        self.assertEqual(weekday, 2005)

        retcode = main(("--year", "2001", "--month", "1", "--day", "3"))
        self.assertEqual(retcode, 0)

        retcode = main(("--year", "20011", "--month", "1", "--day", "3"))
        self.assertEqual(retcode, None)

        retcode = main(("--year", "2001", "--month", "13", "--day", "3"))
        self.assertEqual(retcode, None)

        retcode = main(("--year", "2001", "--month", "31", "--day", "32"))
        self.assertEqual(retcode, None)

        weekday = calculate(2017, 5, 9)
        self.assertEqual(weekday, 1)

        weekday = calculate(2017, 4, 31)
        self.assertFalse(weekday == 0)

        weekday = calculate(2016, 2, 29)
        self.assertEqual(weekday, 0)

        weekday = calculate(2017, 2, 29)
        self.assertEqual(weekday, 3)


if __name__ == '__main__':
    unittest.main()
