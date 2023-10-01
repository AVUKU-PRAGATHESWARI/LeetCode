class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        new = sorted(heights)
        l = len(new)
        r = sum(new[i]!=heights[i] for i in range(l))
        return r