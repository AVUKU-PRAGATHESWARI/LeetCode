class Solution:
    def numberOfMatches(self, n: int) -> int:
        r = 0
        while(n>=2):
            r += n//2
            if n%2==0:
                n = n//2
            else:
                n = n//2 + 1
        return r        