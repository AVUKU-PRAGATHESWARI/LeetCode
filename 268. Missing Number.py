class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = len(nums)*(len(nums)+1)//2
        second = sum(nums)
        return first-second 