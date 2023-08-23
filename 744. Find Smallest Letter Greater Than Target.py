class Solution(object):
    def nextGreatestLetter(self, letters, target):
        if target>=letters[-1] or target<letters[0]:
            return letters[0]
        start=0
        end=len(letters)-1
        while(start<=end):
            mid=(start+end)//2
            if target<letters[mid]:
                end=mid-1
            elif target>=letters[mid]:
                start=mid+1 
        return letters[start]
