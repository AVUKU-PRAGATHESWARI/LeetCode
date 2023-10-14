class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        r = n if n%2==0 else n*2
        return r
           