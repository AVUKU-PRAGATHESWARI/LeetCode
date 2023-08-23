class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        new=[]
        for i in image:
            new.append(i[::-1])
        for i in range(len(new)):
            for j in range(len(new[i])):
                if new[i][j]==0:
                    new[i][j]=1 
                else:
                    new[i][j]=0
        return new
