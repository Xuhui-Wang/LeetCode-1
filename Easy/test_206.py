import unittest
from lc_206_ReverseLinkedList import Solution
from ListNode import ListNode


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_solution(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head_reversed = self.sol.reverseList(head)
        self.assertEqual(head_reversed.val, 3, 'Incorrect 1st result')
        self.assertEqual(head_reversed.next.val, 2, 'Incorrect 1st result')
        self.assertEqual(head_reversed.next.next.val, 1, 'Incorrect 1st result')
        self.assertIsNone(head_reversed.next.next.next, 'Should be null')

    def tearDown(self):
        del self.sol
