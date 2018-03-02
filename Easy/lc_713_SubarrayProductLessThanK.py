class Solution:
    # 2 pointers, O(N) time, O(1) space solution
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start, prod, res = 0, 1, 0
        for i in range(len(nums)):
            prod *= nums[i]
            while start <= i and prod >= k:
                prod /= nums[start]
                start += 1
            res += (i - start + 1)
        return res
