class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        result = 0
        length = len(pref)
        for i in words:
            if i[:length] == pref:
                result += 1 
        return result
        