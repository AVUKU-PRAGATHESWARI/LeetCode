class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        total = prices[0]+prices[1] 
        result = money
        if total <= money:
            return result-total
        else:
            return result                 