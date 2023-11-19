class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = [pref[0]]        
        n = len(pref)
        for i in range(1,n):
            ele = pref[i-1] ^ pref[i]
            print(ele,pref[i-1],pref[i])
            res.append(ele)
        return res