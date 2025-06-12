class Solution:

    # @param n, a 32-bit integer
    # @return an integer

    def reverseBits(self, n):
        reverse = 0
        for _ in range(32):
            reverse = (reverse << 1) | (n & 1)
            n = n >> 1
        return reverse