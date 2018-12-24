import unittest
from lc_964_leastOperators import Solution


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        self.assertEqual(5, self.sol.leastOpsExpressTarget(3, 19), 'Incorrect lists result')
        self.assertEqual(8, self.sol.leastOpsExpressTarget(5, 501), 'Incorrect lists result')
        self.assertEqual(3, self.sol.leastOpsExpressTarget(100, 100000000), 'Incorrect lists result')

    def tearDown(self):
        del self.sol
