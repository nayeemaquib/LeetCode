class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if n <= 1:
            return n

        prev = nums[0]
        start = 0

        for i in range(1, n):
            if nums[i] != prev:
                start += 1
                # Everytime I find a new non-repeat element, I put it at the end of the no-repeat sublist
                nums[i], nums[start] = nums[start], nums[i]
                prev = nums[start]
        return start + 1