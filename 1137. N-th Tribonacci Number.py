class Solution:
    def tribonacci(self, n: int) -> int:
        T = [0,1,1]
        for i in range(3,n+1):
            s = T[i-1] + T[i-2] + T[i-3]
            T.append(s)
        r = T[n]
        return r