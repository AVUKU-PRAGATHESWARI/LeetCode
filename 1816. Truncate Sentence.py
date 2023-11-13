class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        stringsplit = s.split()
        result = stringsplit[:k]
        return " ".join(result)
