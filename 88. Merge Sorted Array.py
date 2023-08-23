class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if m < 1:
            nums1[:] = nums2[:n]
        elif n <1:
            nums1[:] = nums1[:m]
        else:
            nums1[:] = sorted(nums1[:m] + nums2[:n]) 