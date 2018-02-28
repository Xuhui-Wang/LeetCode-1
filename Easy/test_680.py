import unittest
from lc_680_ValidPalindrome import Solution


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        s = "deeee"
        self.assertTrue(self.sol.validPalindrome(s))

    def tearDown(self):
        del self.sol
