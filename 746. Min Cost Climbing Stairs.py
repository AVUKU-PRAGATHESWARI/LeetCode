class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(len(cost)-4, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        res = min(cost[0],cost[1])
        return res