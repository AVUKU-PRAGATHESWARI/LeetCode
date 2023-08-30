class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        first = nums[-2]*nums[-1]
        second = nums[0]*nums[1]
        return first-second
