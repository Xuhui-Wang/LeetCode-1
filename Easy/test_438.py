import unittest
from lc_438_FindAllAnagrams import Solution


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        s, p = "cbaebabacd", "abc"
        expected = [0, 6]
        self.assertEqual(self.sol.findAnagrams(s, p), expected)

    def test_solution2(self):
        s, p = "abab", "ab"
        expected = [0, 1, 2]
        self.assertEqual(self.sol.findAnagrams(s, p), expected)

    def tearDown(self):
        del self.sol
