class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        result = []
        N = len(nums)
        for i in range(N):
            prefix = len(set(nums[:i+1]))
            suffix = len(set(nums[i+1:]))
            result.append(prefix-suffix)
        return result