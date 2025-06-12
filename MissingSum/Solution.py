class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums length is at least 1 
        # O(n^2) complexity 
        # for i in range(0, max(nums) + 1):
        #     if i not in nums:
        #         return i
        
        # return max(nums) + 1

        # O(n) complexity
        nums_set = set()
        
        for i in nums:
            nums_set.add(i)
        
        for i in range(0, max(nums) + 1):
            if i not in nums_set:
                return i 
        
        return max(nums) + 1
