class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        n = 0
        l = a if a<b else b
        for i in range(1,l+1):
            if a%i==0 and b%i==0:
                n += 1
        return n
        