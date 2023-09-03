class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        N = len(s)
        result = ['']*(N)
        for i in s:
            index = int(i[-1])-1
            result[index] = i[:len(i)-1] 
        return ' '.join(result)
