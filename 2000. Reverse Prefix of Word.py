class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word = list(word)
        if ch in word:
            last = word.index(ch)
            first = 0
            while(first<last):
                temp = word[first]
                word[first] = word[last]
                word[last] = temp
                first += 1
                last -= 1
        return ''.join(word)