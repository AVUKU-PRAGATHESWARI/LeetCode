class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range(len(nums)):
            left_sum = sum(nums[:i])
            print(left_sum)
            right_sum = sum(nums[i+1:])
            print(right_sum)
            result.append(abs(left_sum - right_sum))
        return result

# https://leetcode.com/problems/left-and-right-sum-differences/description/