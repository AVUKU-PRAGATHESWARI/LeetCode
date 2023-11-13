class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        start = max(nums)
        sum = 0
        for i in range(start,start+k):
            sum += i
        return sum