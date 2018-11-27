import unittest
from army_rank import solution


class WidgetTestCase(unittest.TestCase):

    def test_rank(self):
        self.assertEqual(5, solution([3, 4, 3, 0, 2, 2, 3, 0, 0]), 'Incorrect lists result')
        self.assertEqual(0, solution([4, 2, 0]), 'Incorrect lists result')
        self.assertEqual(3, solution([4, 4, 3, 3, 1, 0]), 'Incorrect lists result')
