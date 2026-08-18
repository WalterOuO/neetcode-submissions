class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Bottom-up Dynamic Programming
        
        # dp array: store solution form [0 ~ amount]
        # default value as amount + 1
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >=0:
                    dp[a] = min(dp[a], 1 + dp[a-c])

        # not return default value
        if dp[amount] != amount + 1:
            return dp[amount]
        else:
            return -1
        
        # Evaluation
        ## Time: O(amount * coins)
        ## Space: O(amount) for dp array