class Solution:
    # O(N) time, O(N) space
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
