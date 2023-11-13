class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        new = str(num)
        if num != 0 and new[-1]=='0':
            return 0
        return 1
        