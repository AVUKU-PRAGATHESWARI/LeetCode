class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = [0]*len(nums)
        for i in range(len(nums)):
            value = nums[i]
            index_tar = index[i]
            target = target[:index_tar]+[value]+target[index_tar:]
            target.pop()
        return target
