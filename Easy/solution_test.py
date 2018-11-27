import unittest
from solution import solution


class WidgetTestCase(unittest.TestCase):

    def test_solution(self):
        self.assertEqual("upper", solution("ABC"), 'Incorrect lists result')
        self.assertEqual("lower", solution("aBC"), 'Incorrect lists result')
        self.assertEqual("digit", solution("10BC"), 'Incorrect lists result')
        self.assertEqual("other", solution("@BC"), 'Incorrect lists result')
