class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # Initial solution: Runtime only beats 5% of solutions on LeetCode
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if (not i == j) and (nums[i] + nums[j] == target):
        #             return [i, j]

        # Another solution
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]