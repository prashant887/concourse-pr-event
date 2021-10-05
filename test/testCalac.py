import unittest
from src.Calculator import Calculator


class CalcTestCases(unittest.TestCase):
    def test_sum(self):
        calc = Calculator(8, 4)
        res = calc.sum()
        self.assertEqual(res, 12)  # add assertion here

    def test_diff(self):
        calc = Calculator(8, 4)
        res = calc.diff()
        self.assertEqual(res, 4)


if __name__ == '__main__':
    unittest.main()
