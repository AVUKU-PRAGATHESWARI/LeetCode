class Solution(object):
    def removeElement(self, nums, val):
        if len(nums) == 0:
            return 0
        
        while val in nums:
            nums.remove(val)  