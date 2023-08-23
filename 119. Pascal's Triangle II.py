class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        index=[]
        for i in range(rowIndex+1):
            if i==0:
                index=[1]
            elif i==1:
                index=[1,1]
            else:
                index1=[1]
                for j in range(len(index)-1):
                    add=index[j]+index[j+1]
                    index1.append(add)
                index1.append(1)
                index=index1
        return index
 