class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        e = [i for i in nums if i%2==0]
        o = [i for i in nums if i%2==1]
        index = 0
        for i in range(1,len(nums),2):
            nums[i-1],nums[i] = e[index], o[index]
            index += 1
        return nums