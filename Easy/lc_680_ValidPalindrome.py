class Solution:
    def _isPalindrome(self, s, lo, hi):
        while lo < hi:
            if s[lo] != s[hi]:
                return False
            lo, hi = lo + 1, hi - 1
        return True

    # using Two pointers, O(N) time, O(1) space
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(int(len(s) / 2)):
            j = len(s) - i - 1
            if s[i] != s[j]:
                return self._isPalindrome(s, i + 1, j) or self._isPalindrome(s, i, j - 1)

        return True
