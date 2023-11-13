class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum=0
        summing=[]
        for i in nums:
            sum+=i
            summing.append(sum)
        return summing