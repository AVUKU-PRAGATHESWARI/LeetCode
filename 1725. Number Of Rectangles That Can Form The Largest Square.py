class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        temp = []
        for i in rectangles:
            temp.append(min(i))
        max_square = max(temp)
        return temp.count(max_square)
    