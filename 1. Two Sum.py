class Solution(object):
    def twoSum(self, nums, target):
        li=[]
        mp=False
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if target==nums[i]+nums[j]:
                    li.append(i)
                    li.append(j)
                    break
        return li
        
