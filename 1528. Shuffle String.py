class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = ['']*len(indices)
        print(result)
        for i in range(len(indices)):
            index = indices[i]
            result[index] = s[i]
        print(result)
        return ''.join(result)
    