class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        result = 0
        while(nums):
            if len(nums)<=1:
                result += nums[0]
                break
            curr = int(str(nums[0])+str(nums[-1]))
            result += int(curr)
            del nums[0]
            del nums[-1]
        return result