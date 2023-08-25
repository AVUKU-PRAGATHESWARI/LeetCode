class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        if nums[0]<0 & nums[1]<0:
            result = (nums[0]-1) * (nums[1]-1)
        result = max(result,(nums[-1]-1) * (nums[-2]-1))
        return result