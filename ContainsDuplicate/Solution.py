class Solution(object):

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_set = set()
        for i in nums:
            nums_set.add(i)
        return len(nums_set) != len(nums)