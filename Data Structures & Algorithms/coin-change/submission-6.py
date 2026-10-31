class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # bottom-up DP
        if amount == 0:
            return 0

    # 因為題目所求是最少硬幣數, so 設初始值(amount+1)>全用1元湊amount所需硬幣數
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        # 1 ~ 12
        for a in range(1, amount+1):
            # coins = [1, 5, 10]
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1 + dp[ a-coin ])
        
        return -1 if dp[amount] >= (amount +1) else dp[amount]
        
        # Evaluation
        ## Time: O(amount * coins)
        ## Space: O(amount)