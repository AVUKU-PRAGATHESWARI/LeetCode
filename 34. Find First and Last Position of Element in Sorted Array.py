class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result=[]
        if nums.count(target)<1:
            return [-1,-1]
        for i in range(len(nums)):
            if nums[i]==target:
                result.append(i)
                break
        for j in range(len(nums)-1,-1,-1):
            if nums[j]==target:
                result.append(j)
                break
        return result 