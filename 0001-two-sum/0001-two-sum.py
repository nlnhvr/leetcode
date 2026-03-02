class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            val = nums[i]
            if target - val in dic:
                return [dic[target-val],i]
            else: dic[val] = i
