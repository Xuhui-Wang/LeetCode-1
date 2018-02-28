class Solution:
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxLen, sum = 0, 0
        map = {0: -1}
        for i in range(len(nums)):
            sum += nums[i]
            if sum - k in map:
                maxLen = max(maxLen, i - map[sum - k])
            if sum not in map:
                map[sum] = i
        return maxLen
