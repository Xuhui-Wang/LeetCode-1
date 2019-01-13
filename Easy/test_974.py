import unittest
from lc_974_subarraySumsDivisableK import Solution


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        A = [4, 5, 0, -2, -3, 1]
        K = 5
        self.assertEqual(self.sol.subarraysDivByK(A, K), 7)

    def tearDown(self):
        del self.sol
