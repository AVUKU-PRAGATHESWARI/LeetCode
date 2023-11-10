class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        left = 0
        right = len(s)-1
        s = list(s)
        while(left<right):
            if s[left] != s[right]:
                mini = min(s[left],s[right])
                s[left] = mini
                s[right] = mini
            left += 1
            right -= 1
        return "".join(s)