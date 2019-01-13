import unittest
from lc_976_largestPerimeterTriangle import Solution


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution1(self):
        A = [2, 1, 2]
        self.assertEqual(self.sol.largestPerimeter(A), 5)

    def test_solution2(self):
        A = [1, 2, 1]
        self.assertEqual(self.sol.largestPerimeter(A), 0)

    def test_solution3(self):
        A = [3,2,3,4]
        self.assertEqual(self.sol.largestPerimeter(A), 10)

    def test_solution4(self):
        A = [3,6,2,3]
        self.assertEqual(self.sol.largestPerimeter(A), 8)

    def tearDown(self):
        del self.sol
