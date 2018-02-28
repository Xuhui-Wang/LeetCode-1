class Solution:
    # iterative solution - O(N) time, O(1) space
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, cur, next = None, head, None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev
