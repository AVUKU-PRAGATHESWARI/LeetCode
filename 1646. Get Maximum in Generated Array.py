class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0,1]
        if n==0:
            return 0
        for i in range(2,n+1):
            j = i//2
            if i%2==0:
                nums.append(nums[j])
            else:
                nums.append(nums[j] + nums[j+1])
        return max(nums)
