class Solution:
    def addDigits(self, num: int) -> int:
        res = num%9
        if num==0:
            return 0
        elif res==0:
            return 9
        else:
            return res