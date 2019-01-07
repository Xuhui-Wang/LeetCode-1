import unittest
from lc_972_equalRationalNumbers import Solution


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        s, t = "0.(52)", "0.5(25)"
        self.assertTrue(self.sol.isRationalEqual(s, t))

    def test_solution2(self):
        s, t = "0.1666(6)", "0.166(66)"
        self.assertTrue(self.sol.isRationalEqual(s, t))

    def test_solution3(self):
        s, t = "0.9(9)", "1."
        self.assertTrue(self.sol.isRationalEqual(s, t))

    def tearDown(self):
        del self.sol
