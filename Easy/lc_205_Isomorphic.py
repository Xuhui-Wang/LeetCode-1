import sys


class Solution:
    # O(N) solution using counting array, O(26) space
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count1, count2 = [0] * 256, [0] * 256
        for i in range(len(s)):
            c1, c2 = s[i], t[i]
            index1, index2 = ord(c1), ord(c2)
            if count1[index1] != count2[index2]:
                return False
            count1[index1], count2[index2] = i + 1, i + 1
        return True
