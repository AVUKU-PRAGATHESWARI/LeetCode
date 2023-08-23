class Solution(object):
    def generate(self, numRows):
        result=[]
        for i in range(1,numRows+1):
            if i==1:
                index=[1]
            elif i==2:
                index=[1,1]
            else:
                index2=[]
                index2.append(1)
                for i in range(len(index)-1):
                    sum=index[i]+index[i+1]
                    index2.append(sum)
                index2.append(1)
                index=index2
            result.append(index)
        return result