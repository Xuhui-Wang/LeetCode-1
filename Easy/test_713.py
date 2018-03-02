import unittest
from lc_713_SubarrayProductLessThanK import Solution


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        nums = [10, 5, 2, 6]
        k = 100
        self.assertEqual(self.sol.numSubarrayProductLessThanK(nums, k), 8)

    def test_solution2(self):
        nums = [1, 2, 3]
        k = 0
        self.assertEqual(self.sol.numSubarrayProductLessThanK(nums, k), 0)


    def tearDown(self):
        del self.sol
