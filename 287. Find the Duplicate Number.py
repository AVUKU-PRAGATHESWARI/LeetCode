class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i=0
        while(i<len(nums)):
            correct=nums[i]-1
            if(nums[i]<=0 or nums[i]>len(nums)):
                i=i+1
                continue
            if(nums[i]!=nums[correct]):
                nums[i],nums[correct]=nums[correct],nums[i]
            else:
                i=i+1
        for i in range(0,len(nums)):
            if nums[i]!=(i+1):
                return nums[i] 