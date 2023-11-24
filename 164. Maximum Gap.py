class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        for i in range(1,len(nums)):
            curr = abs(nums[i-1]-nums[i])
            res = max(res,curr)
        return res