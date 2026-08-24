class Solution:
    def countBits(self, n: int) -> List[int]:
        # dp : most significant bit
        # most significant bit: [1, 2, 4, 8, 16...]
        dp = [0]* (n+1)
        dp[0] = 0
        msnfbit = 1
        for i in range(1, n+1):
            if i == 2*msnfbit:
                msnfbit = i
            dp[i] = 1 + dp[i-msnfbit]

        return dp

        