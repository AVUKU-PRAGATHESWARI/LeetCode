class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        stepcount=1
        result = 0
        while(stepcount<=len(arr)):
            for i in range(0,len(arr)-stepcount+1):
                new_arr = arr[i:i+stepcount]
                result += sum(new_arr)
            stepcount += 2
        return result