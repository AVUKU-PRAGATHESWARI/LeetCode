class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n==0:
            return nums
        elif n==1:
            return [str(nums[0])]
        start = nums[0]
        end = nums[0] 
        res = []
        for i in range(1,n):
            if (end+1) == nums[i]: 
                end += 1
            else:
                if start == end:
                    ele = str(start)
                else:
                    ele = str(start)+"->"+str(end)
                res.append(ele) 
                start = nums[i]
                end = nums[i] 
        if start == end:
            ele = str(start)
        else:
            ele = str(start)+"->"+str(end)
        res.append(ele)
        return res