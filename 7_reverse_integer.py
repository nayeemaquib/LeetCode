class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = (x>0) - (x<0)
        new_x = int(str(abs(x))[::-1])
        if new_x > 2**31:
            return 0
        return sign*new_x