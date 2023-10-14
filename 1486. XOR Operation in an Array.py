class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        r = 0
        for i in range(start,start+2*n,2):
            r ^= i
        return r