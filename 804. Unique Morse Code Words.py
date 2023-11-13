class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alphabet = {'a':".-",
        'b':"-...",
        'c':"-.-.",
        'd':"-..",
        'e':".",
        'f':"..-.",
        'g':"--.",
        'h':"....",
        'i':"..",
        'j':".---",
        'k':"-.-",
        'l':".-..",
        'm':"--",
        'n':"-.",
        'o':"---",
        'p':".--.",
        'q':"--.-",
        'r':".-.",
        's':"...",
        't':"-",
        'u':"..-",
        'v':"...-",
        'w':".--",
        'x':"-..-",
        'y':"-.--",
        'z':"--.."}
        result = []
        for i in words:
            midstring = ''
            for j in i:
                midstring += alphabet[j]
            result.append(midstring)
        return len(list(set(result)))










