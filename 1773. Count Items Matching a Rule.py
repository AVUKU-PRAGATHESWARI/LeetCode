class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        result = 0
        if ruleKey == "type":
            for i in items:
                if i[0]==ruleValue:
                    result+=1
        elif ruleKey == "color":
            for i in items:
                if i[1]==ruleValue:
                    result+=1
        elif ruleKey == "name":
            for i in items:
                if i[2]==ruleValue:
                    result+=1
        return result