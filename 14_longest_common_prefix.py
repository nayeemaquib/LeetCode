class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]

        mins = min(strs, key=len)
        n = len(mins)
        i = 0
        while i < len(strs):
            if mins[:n] != strs[i][:n]:
                n -= 1
                i = 0
            else:
                i += 1

        return mins[:n]
