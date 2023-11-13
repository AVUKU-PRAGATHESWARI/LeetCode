class Solution(object):
    def searchInsert(self, nums, target):
        index=0
        if target in nums:
            return nums.index(target)
        for i in range(len(nums)):
            if nums[i]<target:
                index=index+1
            else:
                break
        return index 