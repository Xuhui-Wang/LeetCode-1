import unittest
from lc_973_kClosest import Solution


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution1(self):
        points = [[1, 3], [-2, 2]]
        K = 1
        exp = [[-2, 2]]
        self.assertEqual(self.sol.kClosest(points, K), exp)

    def test_solution2(self):
        points = [[3,3],[5,-1],[-2,4]]
        K = 2
        exp = [[3,3],[-2,4]]
        self.assertEqual(self.sol.kClosest(points, K), exp)

    def tearDown(self):
        del self.sol
