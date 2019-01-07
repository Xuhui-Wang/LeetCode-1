import unittest
from lc_969_pancake_sorting import Solution, reverse


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        x = [3, 2, 4, 1]
        ans = self.sol.pancakeSort(x)
        for k in ans:
            reverse(ans, 0, k - 1)
        self.assertEqual(x, [1, 2, 3, 4])

    def tearDown(self):
        del self.sol
