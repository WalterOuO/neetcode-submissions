class Solution:
    def countBits(self, n: int) -> List[int]:
        # dp : 2 power num [1, 2, 4, 8, 16...]
        # when n = 2 power num: looks like 1000000 (only one 1)
        # offset of dp should be 2 power num
        dp = [0]* (n+1)
        dp[0] = 0
        twopowernum = 1
        for i in range(1, n+1):
            if i == 2*twopowernum:
                twopowernum = i
            dp[i] = 1 + dp[i-twopowernum]

        return dp

        