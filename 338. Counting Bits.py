class Solution:
    def countBits(self, n: int) -> List[int]:
        r = []
        for i in range(0,n+1):
            b = bin(i)
            n = b.count('1')
            r.append(n)
        return r 