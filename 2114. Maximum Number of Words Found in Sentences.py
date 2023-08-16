class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        result = 0
        for i in sentences:
            count = 0
            list1 = i.split(" ")
            result = max(result,len(list1))
        return result