class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        add = 0
        once= True
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i==j or j==(len(mat)-i-1):
                    if once and i==(len(mat)//2) and j==(len(mat)//2):
                        once = False
                        add += mat[i][j]
                    else:
                        add += mat[i][j]
        return add
    