class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result = 0
        i=0
        r_count = 0
        l_count = 0
        while(i<len(s)):
            if s[i]=='R':
                r_count += 1
                i+=1
            else:
                l_count += 1
                i += 1
            if r_count==l_count:
                result += 1
        return result
