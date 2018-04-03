class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        d = {"I": 1,
             "V": 5,
             "X": 10,
             "L": 50,
             "C": 100,
             "D": 500,
             "M": 1000}

        res = 0
        prev = 0

        for i in s[::-1]:
            value = d[i]
            if value >= prev:
                res += value
            else:
                res -= value
            prev = value

        return res
