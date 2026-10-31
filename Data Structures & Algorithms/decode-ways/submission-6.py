class Solution:
    def numDecodings(self, s: str) -> int:
        # bottom-up
        if not s or s[0] == '0':
            return 0

        n = len(s)

        dp = [0] * (n+1)    # dp[1]~dp[n] 對應 s[0]~s[n-1] 的方法數
        dp[0] = 1   # 代表在 起始之前的方法數, 設為 1 方便 s[1] 合併解碼使用
        dp[1] = 1   # 代表在 s[0] 時的方法數

        # s = '22018'
        # dp= 112112
        # 從 s[1] 開始解碼, s[0] 的方法數在 dp[1]
        for i in range(2, n+1):
            # 若自己 != 0 則可單獨解碼 
            if s[i-1] != '0':
                dp[i] += dp[i-1]

            # 與前者合併解碼
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        
        return dp[n]