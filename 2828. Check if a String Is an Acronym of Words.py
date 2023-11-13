class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        newstr = ''
        for i in words:
            newstr += i[0]
        if newstr == s:
            return True
        return False