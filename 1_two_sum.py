# O(n)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        res = []

        for i in range(0, len(nums)):
            if (target - nums[i]) in d:
                res.append(i)
                res.append(d[target - nums[i]])
                return res
            else:
                d[nums[i]] = i
        return res
