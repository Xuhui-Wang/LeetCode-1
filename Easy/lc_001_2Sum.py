class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        dict = {}
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in dict:
                return [dict[remain], i]
            else:
                dict[nums[i]] = i
        return True
