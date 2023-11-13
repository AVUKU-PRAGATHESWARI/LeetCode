class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = nums1+nums2
        total.sort()
        length = len(total)
        if (length % 2 == 0):
            mid1 = total[length//2-1]
            mid2 = total[length//2]
            result = (mid1+mid2)/2
        else:
            result = total[length//2]
        return round(result,5)
 