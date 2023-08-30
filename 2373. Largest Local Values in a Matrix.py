class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        result = []
        for i in range(len(grid)-2):
            row = []
            for j in range(len(grid[i])-2):
                element = 0
                element = max(element,max(grid[i][j:j+3]))
                element = max(element,max(grid[i+1][j:j+3]))
                element = max(element,max(grid[i+2][j:j+3]))
                row.append(element)
                print(element)
            result.append(row)
        return result