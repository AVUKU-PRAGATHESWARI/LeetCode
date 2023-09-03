class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = []
        N = len(prices)
        for i in range(N):
            for j in range(i+1,N):
                if prices[j] <= prices[i]:
                    result.append(prices[i]-prices[j])
                    break 
                if j==N-1:
                    result.append(prices[i])
        result.append(prices[-1])
        return result