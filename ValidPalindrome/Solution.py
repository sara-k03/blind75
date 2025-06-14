class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # Solution 1 - O(n^2)
        # reverse = []
        # s_arr = []
        # for i in s:
        #     if i.isalnum():
        #         s_arr.append(i.lower())
        #         reverse.insert(0, i.lower())
        
        # return reverse == s_arr

        # Solution 2 - O(n)
        s_arr = []
        for j in s:
            if j.isalnum():
                s_arr.append(j)

        for i in range( int( len(s_arr) / 2 ) ):
            if not s_arr[i].lower() == s_arr[-i - 1].lower():
                return False
        
        return True