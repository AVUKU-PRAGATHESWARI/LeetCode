class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result = [0,0]
        result[0] = set(nums1) - set(nums2)
        result[1] = set(nums2) - set(nums1)
        return result
     
        