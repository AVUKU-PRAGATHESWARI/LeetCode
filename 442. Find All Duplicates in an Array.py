class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result=[]
        i=0
        while(i<len(nums)):
            correct=nums[i]-1
            if(nums[i]!=nums[correct]):
                nums[i],nums[correct]=nums[correct],nums[i]
            else:
                i=i+1
        for i in range(len(nums)):
            if(nums[i]!=(i+1)):
                result.append(nums[i])
        return result
            
        