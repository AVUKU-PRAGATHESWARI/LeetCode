class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for i in nums:
            for j in str(i):
                result.append(int(j))
        return result