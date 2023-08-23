class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result = 0
        for i in words:
            count = 0
            for j in i:
                if j in allowed:
                    count += 1
            if count == len(i):
                result += 1
        return result  