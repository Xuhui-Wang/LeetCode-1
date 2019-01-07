import unittest
from lc_970_powerfulInteger import Solution


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        x, y, bound = 2, 3, 10
        expected = [2,3,4,5,7,9,10]
        self.assertEqual(self.sol.powerfulIntegers(x, y, bound), expected)

    def test_solution2(self):
        x, y, bound = 3, 5, 15
        expected = [2,4,6,8,10,14]
        self.assertEqual(self.sol.powerfulIntegers(x, y, bound), expected)

    def test_solution3(self):
        x, y, bound = 1, 1, 0
        expected = []
        self.assertEqual(self.sol.powerfulIntegers(x, y, bound), expected)

    def test_solution4(self):
        x, y, bound = 1, 1, 2
        expected = [2]
        self.assertEqual(self.sol.powerfulIntegers(x, y, bound), expected)

    def test_solution5(self):
        x, y, bound = 1, 1, 1
        expected = []
        self.assertEqual(self.sol.powerfulIntegers(x, y, bound), expected)

    def tearDown(self):
        del self.sol
