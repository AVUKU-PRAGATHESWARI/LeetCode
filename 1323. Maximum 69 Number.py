class Solution:
    def maximum69Number (self, num: int) -> int:
        s = list(str(num))
        if '6' in s:
            index = s.index('6')
            s[index] = '9'
            s = ''.join(s)
            num = int(s)
        return num