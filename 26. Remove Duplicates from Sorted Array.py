class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num=list(set(nums))
        nums.clear()
        nums.extend(num)
        nums.sort()
        return len(nums) 