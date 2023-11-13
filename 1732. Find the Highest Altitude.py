class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = 0
        temp = 0
        for i in gain:
            temp += i
            result = max(result,temp)
        return result
        