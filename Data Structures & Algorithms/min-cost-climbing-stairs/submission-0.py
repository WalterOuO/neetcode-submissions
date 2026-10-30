class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # [1, 2, 3]
        #       |
        # # [1, 2, 1, 2, 1, 1, 1]
        #                   1  1
        n = len(cost)
        dp = [0] * (n+1)
        dp[0], dp[1] = 0, 0

        for i in range(n-1):
            dp[i+2] = min(dp[i+1] + cost[i+1], dp[i] + cost[i])

        return dp[n]