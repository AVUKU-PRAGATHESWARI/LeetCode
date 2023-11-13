class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxArea = 0
        while left<right:
            minimum_height = min(height[left],height[right])
            width = right-left
            current_fill = minimum_height*width
            maxArea = max(maxArea,current_fill)
            if(height[left]<height[right]):
                left=left+1
            else:
                right=right-1
        return maxArea
 