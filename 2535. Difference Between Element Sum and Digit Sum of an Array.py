class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        first_sum = 0
        second_sum = 0
        for number in nums:
            first_sum += number
            for  i in str(number):
                second_sum += int(i)
        return abs(first_sum-second_sum)