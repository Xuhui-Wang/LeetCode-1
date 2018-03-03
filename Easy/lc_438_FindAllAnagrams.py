class Solution:
    # O(N) time, O(1) space
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        list_anagram = []
        # return empty list_anagram if either one is empty
        if not s or not p:
            return list_anagram
        count = [0] * 128
        # record each character in p
        for c in p:
            count[ord(c)] += 1
        # 2 pointers
        left = right = 0
        matches = len(p)
        while right < len(s):
            # move right everytime, if the character exists in p's count, decrease the count
            if count[ord(s[right])] > 0:
                matches -= 1
            count[ord(s[right])] -= 1
            right += 1

            # if count == 0 then we have found one anagram
            if not matches:
                list_anagram.append(left)

            if right - left == len(p):
                if count[ord(s[left])] >= 0:
                    matches += 1
                count[ord(s[left])] += 1
                left += 1

        return list_anagram
