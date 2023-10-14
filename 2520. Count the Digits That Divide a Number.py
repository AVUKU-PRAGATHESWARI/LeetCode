class Solution:
    def countDigits(self, num: int) -> int:
        r = 0
        t = num
        for i in str(num):
            c = t%int(i) 
            if c==0:
                r+=1
        return r