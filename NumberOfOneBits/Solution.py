class Solution(object):

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        hamming_weight = 0
        while n != 0:
            if n & 1 == 1:
                hamming_weight += 1
            n = n >> 1
        
        return hamming_weight