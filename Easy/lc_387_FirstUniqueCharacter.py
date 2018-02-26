import sys

class Solution:
    def firstUniqChar(self, s):
        # O(N) solution using counting array
        count = [-sys.maxsize] * 26
        for i in range(len(s)):
            c = s[i]
            index = int(ord(c) - ord('a'))
            oldValue = count[index]
            if oldValue != -sys.maxsize:
                count[index] = sys.maxsize
            else:
                count[index] = i
        indices = [x for i, x in enumerate(count) if x >= 0]
        return min(indices) if indices and min(indices) != sys.maxsize else -1