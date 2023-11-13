class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dictonary = {}
        for i in range(len(names)):
            dictonary[heights[i]] = names[i]
        heights.sort()
        heights = heights[::-1]
        for  i in range(len(heights)):
            names[i] = dictonary[heights[i]]
        return names

        
        