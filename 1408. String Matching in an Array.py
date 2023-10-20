class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        n = len(words)
        for i in range(n):
            new = words[:i]+words[i+1:]
            new = ' '.join(new)
            curr = words[i]
            if curr in new:
                ans.append(curr)
        return ans