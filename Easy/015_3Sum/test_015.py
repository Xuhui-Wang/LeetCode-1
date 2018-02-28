import unittest
import solution


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.sol = solution.Solution()

    def test_solution(self):
        nums = [-1, 0, 1, 2, -1, -4]
        expected = [[-1, 0, 1], [-1, -1, 2]]
        output = self.sol.threeSum(nums)
        expect_sorted = sorted(expected, key=lambda x: str(x[0]) + "," + str(x[1]) + "," + str(x[2]))
        output_sorted = sorted(output, key=lambda x: str(x[0]) + "," + str(x[1]) + "," + str(x[2]))
        self.assertEqual(output_sorted, expect_sorted)

    def tearDown(self):
        del self.sol
