import unittest
from lc_315_countSmallerAfterSelf import Solution


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual([2, 1, 1, 0], self.sol.countSmaller([5, 2, 6, 1]), 'Incorrect lists result')

    def tearDown(self):
        del self.sol
