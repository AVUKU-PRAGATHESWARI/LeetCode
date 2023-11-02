class Solution(object):
    def climbStairs(self, n):
        i, fib = 2, [1,1]
        while i<=n:
            curr = fib[i-2] + fib[i-1]
            fib.append(curr)
            i += 1
        return fib[n]