class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev, curr = 0, 0

        for n in range(2, len(cost)+1):
            prev, curr = curr, min(prev + cost[n-2], curr + cost[n-1])
        
        return curr
        