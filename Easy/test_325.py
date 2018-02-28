import unittest
from lc_325_MaxSizeSubarraySum import Solution


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution1(self):
        nums, k = [1, -1, 5, -2, 3], 3
        self.assertEqual(4, self.sol.maxSubArrayLen(nums, k))

    def test_solution2(self):
        nums, k = [-2, -1, 2, 1], 1
        self.assertEqual(2, self.sol.maxSubArrayLen(nums, k))

    def tearDown(self):
        del self.sol
