class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # bottom-up
        if amount == 0:
            return 0

        dp = [amount + 1] * (amount + 1) # 設定：初始值>全用1元湊amount所需數 
        dp[0] = 0

        # 1 ~ 12
        for a in range(1, amount+1):
            # coins = [1, 5, 10]
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1 + dp[ a-coin ])
        
        return -1 if dp[amount] >= (amount +1) else dp[amount]